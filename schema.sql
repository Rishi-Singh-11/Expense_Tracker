-- Create expenses table
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data for testing
INSERT INTO expenses (amount, category, description, date) VALUES
    (45.50, 'Food', 'Grocery shopping at Walmart', '2024-02-10'),
    (1200.00, 'Rent', 'Monthly apartment rent', '2024-02-01'),
    (50.00, 'Transportation', 'Gas for car', '2024-02-08'),
    (120.00, 'Utilities', 'Electricity bill', '2024-02-05'),
    (35.00, 'Entertainment', 'Movie tickets', '2024-02-09'),
    (80.00, 'Food', 'Dinner with friends', '2024-02-11'),
    (25.00, 'Shopping', 'New headphones', '2024-02-07');