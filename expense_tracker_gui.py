import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime, timedelta

# Database file name
DATA_FILE = 'expenses.json'

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker v3.0")
        self.root.geometry("800x700")
        
        # Data initialization
        self.income = 0.0
        self.data = self.load_data()
        
        # UI Setup (Standardizing on .pack() for main containers to avoid conflicts)
        self.setup_ui()
        self.refresh_table()

    def load_data(self):
        """Loads data from JSON with error handling."""
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_data(self):
        """Saves current data to JSON."""
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def setup_ui(self):
        # --- Income Section ---
        income_frame = ttk.LabelFrame(self.root, text="Financial Summary")
        income_frame.pack(pady=10, padx=10, fill="x")
        
        tk.Label(income_frame, text="Set Monthly Income: $").pack(side="left", padx=5)
        self.income_entry = ttk.Entry(income_frame)
        self.income_entry.pack(side="left", padx=5)
        ttk.Button(income_frame, text="Update Balance", command=self.set_income).pack(side="left", padx=5)
        
        self.balance_label = tk.Label(income_frame, text="Balance: $0.00", font=("Arial", 10, "bold"))
        self.balance_label.pack(side="right", padx=15)

        # --- Input Section ---
        input_frame = ttk.LabelFrame(self.root, text="Entry Management")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Using a sub-frame for grid layout to avoid mixing with .pack() of the root
        grid_inner = tk.Frame(input_frame)
        grid_inner.pack()

        tk.Label(grid_inner, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_input = ttk.Entry(grid_inner)
        self.date_input.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_input.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(grid_inner, text="Category:").grid(row=0, column=2, padx=5, pady=5)
        self.cat_input = ttk.Entry(grid_inner)
        self.cat_input.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(grid_inner, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amt_input = ttk.Entry(grid_inner)
        self.amt_input.grid(row=1, column=1, padx=5, pady=5)

        # --- Button Group ---
        btn_frame = tk.Frame(input_frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Add", command=self.add_item).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update Selected", command=self.update_item).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Search Category", command=self.search_item).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_item).pack(side="left", padx=5)

        # --- Table Section ---
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        cols = ("ID", "Date", "Category", "Amount")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings")
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # --- Analysis Section ---
        ana_frame = tk.Frame(self.root)
        ana_frame.pack(pady=10, fill="x", padx=10)

        ttk.Button(ana_frame, text="Compare Today/Yesterday", command=self.compare_spending).pack(side="left", padx=5)
        ttk.Button(ana_frame, text="Monthly Summary", command=self.show_summary).pack(side="left", padx=5)
        ttk.Button(ana_frame, text="DELETE ALL RECORDS", command=self.clear_all, style="Danger.TButton").pack(side="right", padx=5)

    # --- Core Functions ---
    def set_income(self):
        try:
            self.income = float(self.income_entry.get())
            self.refresh_table()
        except ValueError:
            messagebox.showerror("Input Error", "Income must be a valid number.")

    def add_item(self):
        try:
            date = self.date_input.get()
            cat = self.cat_input.get()
            amt = float(self.amt_input.get())
            if not cat: raise ValueError
            
            new_id = max([item['id'] for item in self.data], default=0) + 1
            self.data.append({"id": new_id, "date": date, "category": cat, "amount": amt})
            self.save_data()
            self.refresh_table()
        except ValueError:
            messagebox.showerror("Error", "Invalid data. Check amount and category.")

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select a record from the list to update.")
            return
        
        item_id = self.tree.item(selected[0])['values'][0]
        for item in self.data:
            if item['id'] == item_id:
                try:
                    item['date'] = self.date_input.get()
                    item['category'] = self.cat_input.get()
                    item['amount'] = float(self.amt_input.get())
                    self.save_data()
                    self.refresh_table()
                    messagebox.showinfo("Success", "Record updated successfully.")
                    return
                except ValueError:
                    messagebox.showerror("Error", "Invalid values for update.")

    def search_item(self):
        query = self.cat_input.get().lower()
        self.tree.delete(*self.tree.get_children())
        for item in self.data:
            if query in item['category'].lower():
                self.tree.insert("", "end", values=(item['id'], item['date'], item['category'], item['amount']))

    def delete_item(self):
        selected = self.tree.selection()
        if not selected: return
        item_id = self.tree.item(selected[0])['values'][0]
        self.data = [i for i in self.data if i['id'] != item_id]
        self.save_data()
        self.refresh_table()

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Danger! This will delete ALL data. Proceed?"):
            self.data = []
            self.save_data()
            self.refresh_table()

    def compare_spending(self):
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        t_sum = sum(i['amount'] for i in self.data if i['date'] == today)
        y_sum = sum(i['amount'] for i in self.data if i['date'] == yesterday)
        
        diff = t_sum - y_sum
        status = "increased" if diff > 0 else "decreased"
        messagebox.showinfo("Comparison", f"Today: ${t_sum:.2f}\nYesterday: ${y_sum:.2f}\nSpending has {status} by ${abs(diff):.2f}")

    def show_summary(self):
        if not self.data: return
        categories = {}
        for i in self.data:
            categories[i['category']] = categories.get(i['category'], 0) + i['amount']
        
        top_cat = max(categories, key=categories.get)
        total = sum(categories.values())
        messagebox.showinfo("Analysis", f"Total Expense: ${total:.2f}\nTop Spending: {top_cat} (${categories[top_cat]:.2f})")

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        total = 0
        for item in self.data:
            self.tree.insert("", "end", values=(item['id'], item['date'], item['category'], item['amount']))
            total += item['amount']
        
        rem_balance = self.income - total
        color = "red" if rem_balance < 0 else "darkgreen"
        self.balance_label.config(text=f"Remaining Balance: ${rem_balance:.2f}", fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    # Add some styling for the danger button
    style = ttk.Style()
    style.configure("Danger.TButton", foreground="black")
    app = ExpenseTrackerApp(root)
    root.mainloop()
