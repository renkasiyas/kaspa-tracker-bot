# ABOUTME: SQLite database module for managing user addresses and tracking data
# ABOUTME: Provides async operations for storing user-address relationships

import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

import aiosqlite

from .migrations import Migrator

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_path: str = "kaspa_tracker.db"):
        self.db_path = db_path

    async def init_db(self):
        """Initialize database and run migrations"""
        migrator = Migrator(self.db_path)
        await migrator.run_migrations()
        logger.info("Database initialized and migrations applied")

    async def add_user(self, user_id: int, username: str = None, first_name: str = None):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR IGNORE INTO users (user_id, username, first_name)
                VALUES (?, ?, ?)
            """,
                (user_id, username, first_name),
            )
            await db.commit()

    async def add_address(self, user_id: int, address: str, label: str = None) -> bool:
        try:
            async with aiosqlite.connect(self.db_path) as db:
                await db.execute(
                    """
                    INSERT INTO addresses (user_id, address, label)
                    VALUES (?, ?, ?)
                """,
                    (user_id, address, label),
                )
                await db.commit()
                return True
        except aiosqlite.IntegrityError:
            return False

    async def remove_address(self, user_id: int, address: str) -> bool:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                DELETE FROM addresses
                WHERE user_id = ? AND address = ?
            """,
                (user_id, address),
            )
            await db.commit()
            return cursor.rowcount > 0

    async def remove_address_by_index(self, user_id: int, index: int) -> Optional[str]:
        async with aiosqlite.connect(self.db_path) as db:
            # Get the address at the specified index (1-based)
            cursor = await db.execute(
                """
                SELECT address, label FROM addresses
                WHERE user_id = ?
                ORDER BY added_at DESC
                LIMIT 1 OFFSET ?
            """,
                (user_id, index - 1),
            )

            row = await cursor.fetchone()
            if not row:
                return None

            address = row[0]
            label = row[1]

            # Delete the address
            await db.execute(
                """
                DELETE FROM addresses
                WHERE user_id = ? AND address = ?
            """,
                (user_id, address),
            )
            await db.commit()

            return f"{label + ' ' if label else ''}({address})"

    async def get_user_addresses(self, user_id: int) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT address, label, added_at, last_checked, last_balance, last_utxo_count
                FROM addresses
                WHERE user_id = ?
                ORDER BY added_at DESC
            """,
                (user_id,),
            )

            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def get_address_by_index(self, user_id: int, index: int) -> Optional[str]:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                SELECT address FROM addresses
                WHERE user_id = ?
                ORDER BY added_at DESC
                LIMIT 1 OFFSET ?
            """,
                (user_id, index - 1),
            )

            row = await cursor.fetchone()
            return row[0] if row else None

    async def update_address_stats(self, user_id: int, address: str, balance: str, utxo_count: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                UPDATE addresses
                SET last_checked = CURRENT_TIMESTAMP,
                    last_balance = ?,
                    last_utxo_count = ?
                WHERE user_id = ? AND address = ?
            """,
                (balance, utxo_count, user_id, address),
            )
            await db.commit()

    async def get_all_tracked_addresses(self) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT DISTINCT a.address, a.user_id, a.last_checked, a.last_balance
                FROM addresses a
                JOIN users u ON a.user_id = u.user_id
                ORDER BY a.last_checked ASC
            """
            )

            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def add_transaction(
        self, user_id: int, address: str, tx_type: str, amount: str, utxo_data: dict
    ):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT INTO transactions (user_id, address, tx_type, amount, utxo_data)
                VALUES (?, ?, ?, ?, ?)
            """,
                (user_id, address, tx_type, amount, json.dumps(utxo_data)),
            )
            await db.commit()

    async def get_unnotified_transactions(self, user_id: int) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT id, address, tx_type, amount, utxo_data, created_at
                FROM transactions
                WHERE user_id = ? AND notified = FALSE
                ORDER BY created_at DESC
            """,
                (user_id,),
            )

            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def mark_transactions_notified(self, transaction_ids: List[int]):
        async with aiosqlite.connect(self.db_path) as db:
            placeholders = ",".join("?" * len(transaction_ids))
            await db.execute(
                f"""
                UPDATE transactions
                SET notified = TRUE
                WHERE id IN ({placeholders})
            """,
                transaction_ids,
            )
            await db.commit()

    async def user_exists(self, user_id: int) -> bool:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                SELECT 1 FROM users WHERE user_id = ?
            """,
                (user_id,),
            )
            result = await cursor.fetchone()
            return result is not None

    async def get_address_count(self, user_id: int) -> int:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                SELECT COUNT(*) FROM addresses WHERE user_id = ?
            """,
                (user_id,),
            )
            result = await cursor.fetchone()
            return result[0] if result else 0

    async def update_address_label(self, user_id: int, address: str, label: str) -> bool:
        """Update the label for an address"""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                UPDATE addresses
                SET label = ?
                WHERE user_id = ? AND address = ?
            """,
                (label, user_id, address),
            )
            await db.commit()
            return True

    async def get_address_info(self, user_id: int, address: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific address for a user"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT * FROM addresses
                WHERE user_id = ? AND address = ?
            """,
                (user_id, address),
            )
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def get_users_by_address(self, address: str) -> List[Dict[str, Any]]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """
                SELECT a.user_id, a.label, u.username, u.first_name
                FROM addresses a
                JOIN users u ON a.user_id = u.user_id
                WHERE a.address = ?
            """,
                (address,),
            )

            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
