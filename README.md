# 💰 Modern Expense Tracker

This is a simple web-based tool I built to help track daily spending. It categorizes expenses and shows a visual breakdown of where the money goes.

**Live Demo:** [https://expense-tracker-w9bh.onrender.com](https://expense-tracker-w9bh.onrender.com)

## 🛠️ What it does
* **Track Expenses:** You can add, edit, or delete your daily costs (Food, Rent, etc.).
* **Dashboard:** Shows your total spending at a glance.
* **Visuals:** Uses a pie chart to show which categories take up most of your budget.
* **Responsive:** The design works on both computer screens and phones.

## 💻 How I built it
* **Python & Flask:** Used for the main logic and handling the web pages.
* **SQLite:** A simple database to store the expense entries.
* **Chart.js:** To create the spending chart on the dashboard.
* **HTML/CSS:** For the layout and modern "glass" look.

## 🚀 Running it yourself
If you want to run this locally:
1. Download the files.
2. Install the needs: `pip install -r requirements.txt`.
3. Set up the database: `python -c "from models import init_db; init_db()"`.
4. Start the app: `python app.py`.

## 📌 Note
Since this is hosted on a free Render server using SQLite, any data added might reset if the server goes to sleep or restarts. This is just a demo project!