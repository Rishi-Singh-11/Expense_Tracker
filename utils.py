from models import get_db_connection
from datetime import datetime

def get_total_expenses():
    """Calculate total of all expenses"""
    conn = get_db_connection()
    result = conn.execute('SELECT SUM(amount) as total FROM expenses').fetchone()
    conn.close()
    return result['total'] if result['total'] else 0.0

def get_category_totals():
    """Get total spending grouped by category"""
    conn = get_db_connection()
    results = conn.execute(
        'SELECT category, SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC'
    ).fetchall()
    conn.close()
    
    # Convert to dictionary
    return {row['category']: row['total'] for row in results}

def get_expenses_by_month(month_offset=0):
    """
    Get expenses filtered by month
    month_offset: 0 for current month, -1 for last month
    """
    today = datetime.now()
    
    # Calculate target month and year
    target_month = today.month + month_offset
    target_year = today.year
    
    # Handle month overflow/underflow
    while target_month < 1:
        target_month += 12
        target_year -= 1
    while target_month > 12:
        target_month -= 12
        target_year += 1
    
    # Query expenses for that month
    conn = get_db_connection()
    expenses = conn.execute(
        '''SELECT * FROM expenses 
           WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
           ORDER BY date DESC''',
        (f'{target_month:02d}', str(target_year))
    ).fetchall()
    conn.close()
    
    return expenses

def get_monthly_total(month_offset=0):
    """Get total expenses for a specific month"""
    expenses = get_expenses_by_month(month_offset)
    return sum(expense['amount'] for expense in expenses)

def format_currency(amount):
    """Format number as currency string"""
    return f"${amount:,.2f}"