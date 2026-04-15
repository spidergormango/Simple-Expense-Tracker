import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime, timedelta

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker (Pro Version)")
        self.root.geometry("800x700")
        
        # Data logic
        self.file_path = "expenses.json"
        self.expenses = self.load_data()
        self.income = 0.0

        # UI Initialization
        self.setup_ui()
        self.refresh_tree()

    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def setup_ui(self):
        # --- Top Section: Income & Balance ---
        top_frame = tk.LabelFrame(self.root, text="Financial Overview", padx=10, pady=10)
        top_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(top_frame, text="Monthly Income: $").grid(row=0, column=0)
        self.income_entry = tk.Entry(top_frame)
        self.income_entry.grid(row=0, column=1)
        tk.Button(top_frame, text="Set Income", command=self.update_balance).grid(row=0, column=2, padx=5)

        self.balance_label = tk.Label(top_frame, text="Remaining Balance: $0.00", font=("Arial", 10, "bold"))
        self.balance_label.grid(row=0, column=3, padx=20)

        # --- Input Section ---
        input_frame = tk.LabelFrame(self.root, text="Add / Update Record", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Category:").grid(row=0, column=2, padx=5)
        self.cat_entry = tk.Entry(input_frame)
        self.cat_entry.grid(row=0, column=3)

        tk.Label(input_frame, text="Amount:").grid(row=1, column=0, pady=5)
        self.amt_entry = tk.Entry(input_frame)
        self.amt_entry.grid(row=1, column=1)

        # Buttons for CRUD
        btn_frame = tk.Frame(input_frame)
        btn_frame.grid(row=1, column=2, columnspan=2, sticky="e")
        tk.Button(btn_frame, text="Add", width=8, command=self.add_item).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Update", width=8, command=self.update_item).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Search", width=8, command=self.search_items).pack(side="left", padx=2)

        # --- Table Section ---
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("ID", "Date", "Category", "Amount")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True)

        # --- Analysis & Control Section ---
        ctrl_frame = tk.Frame(self.root, pady=10)
        ctrl_frame.pack(fill="x", padx=10)

        tk.Button(ctrl_frame, text="Compare (Today vs Yesterday)", command=self.compare_days).pack(side="left", padx=5)
        tk.Button(ctrl_frame, text="Monthly Summary", command=self.monthly_summary).pack(side="left", padx=5)
        tk.Button(ctrl_frame, text="Delete Selected", bg="#ffcccc", command=self.delete_item).pack(side="right", padx=5)
        tk.Button(ctrl_frame, text="DELETE ALL", bg="red", fg="white", command=self.delete_all).pack(side="right", padx=5)

    # --- Logic Methods ---
    def update_balance(self):
        try:
            self.income = float(self.income_entry.get())
            self.refresh_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for income.")

    def add_item(self):
        try:
            date = self.date_entry.get()
            cat = self.cat_entry.get()
            amt = float(self.amt_entry.get())
            if not cat: raise ValueError
            
            new_id = max([e['id'] for e in self.expenses], default=0) + 1
            self.expenses.append({"id": new_id, "date": date, "category": cat, "amount": amt})
            self.save_data()
            self.refresh_tree()
        except ValueError:
            messagebox.showerror("Error", "Invalid Input. Check Amount and Category.")

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a record to update.")
            return
        
        item_id = self.tree.item(selected)['values'][0]
        for exp in self.expenses:
            if exp['id'] == item_id:
                try:
                    exp['date'] = self.date_entry.get()
                    exp['category'] = self.cat_entry.get()
                    exp['amount'] = float(self.amt_entry.get())
                    self.save_data()
                    self.refresh_tree()
                    messagebox.showinfo("Success", "Record updated.")
                    return
                except ValueError:
                    messagebox.showerror("Error", "Invalid update values.")

    def search_items(self):
        keyword = self.cat_entry.get().lower()
        self.tree.delete(*self.tree.get_children())
        for exp in self.expenses:
            if keyword in exp['category'].lower() or keyword in exp['date']:
                self.tree.insert("", "end", values=(exp['id'], exp['date'], exp['category'], exp['amount']))

    def delete_item(self):
        selected = self.tree.selection()
        if not selected: return
        item_id = self.tree.item(selected)['values'][0]
        self.expenses = [e for e in self.expenses if e['id'] != item_id]
        self.save_data()
        self.refresh_tree()

    def delete_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete ALL records?"):
            self.expenses = []
            self.save_data()
            self.refresh_tree()

    def compare_days(self):
        today_str = datetime.now().strftime("%Y-%m-%d")
        yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        today_sum = sum(e['amount'] for e in self.expenses if e['date'] == today_str)
        yesterday_sum = sum(e['amount'] for e in self.expenses if e['date'] == yesterday_str)
        
        msg = f"Today's Spend: ${today_sum:.2f}\nYesterday's Spend: ${yesterday_sum:.2f}\n"
        msg += f"Difference: ${abs(today_sum - yesterday_sum):.2f} "
        msg += "more" if today_sum > yesterday_sum else "less"
        messagebox.showinfo("Comparison", msg)

    def monthly_summary(self):
        if not self.expenses: return
        categories = {}
        for e in self.expenses:
            categories[e['category']] = categories.get(e['category'], 0) + e['amount']
        
        top_cat = max(categories, key=categories.get)
        total = sum(categories.values())
        messagebox.showinfo("Monthly Sum-up", f"Total Spent: ${total:.2f}\nTop Category: {top_cat} (${categories[top_cat]:.2f})")

    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        total_spent = 0
        for exp in self.expenses:
            self.tree.insert("", "end", values=(exp['id'], exp['date'], exp['category'], exp['amount']))
            total_spent += exp['amount']
        
        balance = self.income - total_spent
        self.balance_label.config(text=f"Remaining Balance: ${balance:.2f}", 
                                  fg="red" if balance < 0 else "darkgreen")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
