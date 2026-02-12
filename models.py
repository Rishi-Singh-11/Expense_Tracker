import sqlite3
import os

DATABASE = os.path.join('instance', 'expenses.db')

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

def init_db():
    """Initialize the database with schema"""
    # Create instance folder if it doesn't exist
    os.makedirs('instance', exist_ok=True)
    
    # Connect and create tables
    conn = get_db_connection()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def get_all_expenses():
    """Get all expenses ordered by date descending"""
    conn = get_db_connection()
    expenses = conn.execute(
        'SELECT * FROM expenses ORDER BY date DESC, created_at DESC'
    ).fetchall()
    conn.close()
    return expenses

def get_expense_by_id(expense_id):
    """Get a single expense by ID"""
    conn = get_db_connection()
    expense = conn.execute(
        'SELECT * FROM expenses WHERE id = ?', (expense_id,)
    ).fetchone()
    conn.close()
    return expense

def add_expense(amount, category, description, date):
    """Add a new expense to database"""
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
        (amount, category, description, date)
    )
    conn.commit()
    conn.close()

def update_expense(expense_id, amount, category, description, date):
    """Update an existing expense"""
    conn = get_db_connection()
    conn.execute(
        'UPDATE expenses SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?',
        (amount, category, description, date, expense_id)
    )
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    """Delete an expense from database"""
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()