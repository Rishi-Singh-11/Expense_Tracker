from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import (
    init_db, get_all_expenses, get_expense_by_id,
    add_expense, update_expense, delete_expense
)
from utils import get_total_expenses, get_category_totals, get_expenses_by_month
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize database
try:
    init_db()
except:
    pass  # Database already exists

@app.route('/')
def index():
    """Main dashboard page"""
    # Get filter parameter
    filter_type = request.args.get('filter', 'all')
    
    # Filter expenses based on selection
    if filter_type == 'this_month':
        expenses = get_expenses_by_month(0)
    elif filter_type == 'last_month':
        expenses = get_expenses_by_month(-1)
    else:
        expenses = get_all_expenses()
    
    # Get statistics
    total = get_total_expenses()
    category_totals = get_category_totals()
    
    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        category_totals=category_totals,
        filter_type=filter_type
    )

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new expense"""
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            category = request.form['category']
            description = request.form.get('description', '').strip()
            date = request.form['date']
            
            # Add to database
            add_expense(amount, category, description, date)
            
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error adding expense: {e}")
            return redirect(url_for('add'))
    
    return render_template('form.html', expense=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit an existing expense"""
    expense = get_expense_by_id(id)
    
    if not expense:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            category = request.form['category']
            description = request.form.get('description', '').strip()
            date = request.form['date']
            
            # Update in database
            update_expense(id, amount, category, description, date)
            
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error updating expense: {e}")
            return redirect(url_for('edit', id=id))
    
    return render_template('form.html', expense=expense)

@app.route('/delete/<int:id>')
def delete(id):
    """Delete an expense"""
    try:
        delete_expense(id)
    except Exception as e:
        print(f"Error deleting expense: {e}")
    
    return redirect(url_for('index'))

@app.route('/api/category-data')
def category_data():
    """API endpoint for chart data"""
    category_totals = get_category_totals()
    
    return jsonify({
        'categories': list(category_totals.keys()),
        'amounts': list(category_totals.values())
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)