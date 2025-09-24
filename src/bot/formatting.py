# ABOUTME: Formatting utilities for displaying KAS amounts
# ABOUTME: Provides consistent and readable balance formatting


def format_kas_amount(sompi: int) -> str:
    """Format sompi amount to KAS with proper decimal places and thousands separators"""
    kas = sompi / 100_000_000

    # For large amounts (>= 1M KAS), use K/M/B suffixes
    if kas >= 1_000_000_000:
        return f"{kas/1_000_000_000:,.2f}B KAS"
    elif kas >= 1_000_000:
        return f"{kas/1_000_000:,.2f}M KAS"
    elif kas >= 10_000:
        # Show with thousands separator, no decimals for large amounts
        return f"{kas:,.0f} KAS"
    elif kas >= 1_000:
        # Show with thousands separator and 2 decimals
        return f"{kas:,.2f} KAS"
    elif kas >= 1:
        # Show 2-4 decimals for amounts 1-999
        if kas >= 100:
            return f"{kas:.2f} KAS"
        else:
            return f"{kas:.4f} KAS"
    elif kas >= 0.01:
        # Show 4-6 decimals for small amounts
        return f"{kas:.6f} KAS"
    elif kas > 0:
        # Show 8 decimals for very small amounts
        return f"{kas:.8f} KAS"
    else:
        return "0 KAS"


def format_kas_amount_from_float(kas: float) -> str:
    """Format KAS float amount with proper decimal places and thousands separators"""
    # For large amounts (>= 1M KAS), use K/M/B suffixes
    if kas >= 1_000_000_000:
        return f"{kas/1_000_000_000:,.2f}B KAS"
    elif kas >= 1_000_000:
        return f"{kas/1_000_000:,.2f}M KAS"
    elif kas >= 10_000:
        # Show with thousands separator, no decimals for large amounts
        return f"{kas:,.0f} KAS"
    elif kas >= 1_000:
        # Show with thousands separator and 2 decimals
        return f"{kas:,.2f} KAS"
    elif kas >= 1:
        # Show 2-4 decimals for amounts 1-999
        if kas >= 100:
            return f"{kas:.2f} KAS"
        else:
            return f"{kas:.4f} KAS"
    elif kas >= 0.01:
        # Show 4-6 decimals for small amounts
        return f"{kas:.6f} KAS"
    elif kas > 0:
        # Show 8 decimals for very small amounts
        return f"{kas:.8f} KAS"
    else:
        return "0 KAS"
