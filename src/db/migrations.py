# ABOUTME: Database migration system for managing schema changes
# ABOUTME: Tracks and applies migrations in order on startup

import logging
from typing import List, Tuple

import aiosqlite

logger = logging.getLogger(__name__)


class Migration:
    def __init__(self, version: int, description: str, up_sql: str, down_sql: str = None):
        self.version = version
        self.description = description
        self.up_sql = up_sql
        self.down_sql = down_sql


# Define all migrations in order
MIGRATIONS: List[Migration] = [
    Migration(
        version=1,
        description="Initial schema - clean deployment",
        up_sql="""
            -- Users table - stores Telegram user information
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            -- Addresses table - stores user's tracked Kaspa addresses
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                address TEXT NOT NULL,
                label TEXT,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_checked TIMESTAMP,
                last_balance TEXT,
                last_utxo_count INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
                UNIQUE(user_id, address)
            );

            -- Transactions table - logs notifications sent to users
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                address TEXT NOT NULL,
                tx_type TEXT,
                amount TEXT,
                utxo_data TEXT,
                notified BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
            );

            -- Indexes for performance
            CREATE INDEX IF NOT EXISTS idx_addresses_user_id ON addresses(user_id);
            CREATE INDEX IF NOT EXISTS idx_addresses_address ON addresses(address);
            CREATE INDEX IF NOT EXISTS idx_transactions_user_id ON transactions(user_id);
            CREATE INDEX IF NOT EXISTS idx_transactions_address ON transactions(address);
            CREATE INDEX IF NOT EXISTS idx_transactions_notified ON transactions(notified);
        """,
    ),
]


class Migrator:
    def __init__(self, db_path: str = "kaspa_tracker.db"):
        self.db_path = db_path

    async def init_migration_table(self, db: aiosqlite.Connection):
        """Create migration tracking table"""
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version INTEGER PRIMARY KEY,
                description TEXT,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        await db.commit()

    async def get_current_version(self, db: aiosqlite.Connection) -> int:
        """Get the current schema version"""
        cursor = await db.execute("SELECT MAX(version) FROM schema_migrations")
        result = await cursor.fetchone()
        return result[0] if result[0] is not None else 0

    async def apply_migration(self, db: aiosqlite.Connection, migration: Migration):
        """Apply a single migration"""
        logger.info(f"Applying migration {migration.version}: {migration.description}")

        try:
            # Execute migration SQL
            for statement in migration.up_sql.split(";"):
                statement = statement.strip()
                if statement:
                    await db.execute(statement)

            # Record migration
            await db.execute(
                "INSERT INTO schema_migrations (version, description) VALUES (?, ?)",
                (migration.version, migration.description),
            )
            await db.commit()

            logger.info(f"Migration {migration.version} applied successfully")
        except Exception as e:
            logger.error(f"Failed to apply migration {migration.version}: {e}")
            await db.rollback()
            raise

    async def run_migrations(self):
        """Run all pending migrations"""
        async with aiosqlite.connect(self.db_path) as db:
            # Enable foreign keys
            await db.execute("PRAGMA foreign_keys = ON")

            # Initialize migration tracking
            await self.init_migration_table(db)

            # Get current version
            current_version = await self.get_current_version(db)
            logger.info(f"Current database version: {current_version}")

            # Apply pending migrations
            pending_migrations = [m for m in MIGRATIONS if m.version > current_version]

            if not pending_migrations:
                logger.info("Database is up to date")
                return

            logger.info(f"Found {len(pending_migrations)} pending migrations")

            for migration in pending_migrations:
                await self.apply_migration(db, migration)

            # Get final version
            final_version = await self.get_current_version(db)
            logger.info(f"Database migrated to version {final_version}")

    async def rollback_to(self, target_version: int):
        """Rollback to a specific version (if down migrations are defined)"""
        async with aiosqlite.connect(self.db_path) as db:
            current_version = await self.get_current_version(db)

            if current_version <= target_version:
                logger.info(f"Already at version {current_version}, nothing to rollback")
                return

            # Get migrations to rollback in reverse order
            to_rollback = [
                m
                for m in reversed(MIGRATIONS)
                if target_version < m.version <= current_version and m.down_sql
            ]

            for migration in to_rollback:
                logger.info(f"Rolling back migration {migration.version}: {migration.description}")

                # Execute rollback SQL
                for statement in migration.down_sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        await db.execute(statement)

                # Remove migration record
                await db.execute(
                    "DELETE FROM schema_migrations WHERE version = ?", (migration.version,)
                )
                await db.commit()

                logger.info(f"Rolled back migration {migration.version}")

    async def get_migration_status(self) -> List[Tuple[int, str, bool]]:
        """Get status of all migrations"""
        async with aiosqlite.connect(self.db_path) as db:
            await self.init_migration_table(db)

            cursor = await db.execute("SELECT version FROM schema_migrations")
            applied_versions = {row[0] for row in await cursor.fetchall()}

            status = []
            for migration in MIGRATIONS:
                is_applied = migration.version in applied_versions
                status.append((migration.version, migration.description, is_applied))

            return status
