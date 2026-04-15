import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import datetime

DATA_FILE = 'expenses.json'


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker V2.0")
        self.root.geometry("780x600")
        self.root.resizable(True, True)

        # Load persisted data
        self.data = self.load_data()

        # Build all UI widgets
        self.create_widgets()
        self.update_treeview()

    # ------------------------------------------------------------------ #
    # Data layer                                                           #
    # ------------------------------------------------------------------ #

    def load_data(self):
        """Load expenses from JSON.  Returns [] on missing file or error."""
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            messagebox.showerror(
                "Load Error",
                f"Could not read '{DATA_FILE}'.\nStarting with an empty list."
            )
            return []

    def save_data(self):
        """Persist self.data to JSON.  Shows an error dialog on failure."""
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            messagebox.showerror("Save Error", f"Could not save data:\n{e}")

    # ------------------------------------------------------------------ #
    # UI construction                                                      #
    # ------------------------------------------------------------------ #

    def create_widgets(self):

        # ── Top: Add Expense ─────────────────────────────────────────── #
        input_frame = ttk.LabelFrame(self.root, text="Add New Expense")
        input_frame.pack(pady=8, padx=10, fill="x")

        ttk.Label(input_frame, text="Category:").grid(
            row=0, column=0, padx=6, pady=6, sticky="w")
        self.cat_entry = ttk.Entry(input_frame, width=18)
        self.cat_entry.grid(row=0, column=1, padx=6, pady=6)

        ttk.Label(input_frame, text="Amount ($):").grid(
            row=0, column=2, padx=6, pady=6, sticky="w")
        self.amt_entry = ttk.Entry(input_frame, width=14)
        self.amt_entry.grid(row=0, column=3, padx=6, pady=6)

        ttk.Button(input_frame, text="Add Record",
                   command=self.add_item).grid(row=0, column=4, padx=10, pady=6)

        # Enter-key shortcuts
        self.cat_entry.bind("<Return>", lambda e: self.amt_entry.focus())
        self.amt_entry.bind("<Return>", lambda e: self.add_item())

        # ── Income & Balance row ─────────────────────────────────────── #
        balance_frame = ttk.LabelFrame(self.root, text="Income & Balance")
        balance_frame.pack(pady=4, padx=10, fill="x")

        ttk.Label(balance_frame, text="Monthly Income ($):").grid(
            row=0, column=0, padx=6, pady=6, sticky="w")
        self.income_entry = ttk.Entry(balance_frame, width=14)
        self.income_entry.grid(row=0, column=1, padx=6, pady=6)

        ttk.Button(balance_frame, text="Calculate Balance",
                   command=self.calculate_balance).grid(
            row=0, column=2, padx=10, pady=6)

        self.balance_label = ttk.Label(
            balance_frame, text="Balance: —", font=("Arial", 11, "bold"))
        self.balance_label.grid(row=0, column=3, padx=20, pady=6, sticky="w")

        # ── Expense list (Treeview) ──────────────────────────────────── #
        list_frame = ttk.Frame(self.root)
        list_frame.pack(pady=6, padx=10, fill="both", expand=True)

        columns = ("id", "date", "category", "amount")
        self.tree = ttk.Treeview(
            list_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("id",       text="ID")
        self.tree.heading("date",     text="Date")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount",   text="Amount ($)")
        self.tree.column("id",       width=45,  anchor="center")
        self.tree.column("date",     width=105, anchor="center")
        self.tree.column("category", width=230, anchor="w")
        self.tree.column("amount",   width=110, anchor="e")

        scrollbar = ttk.Scrollbar(
            list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ── Action buttons ───────────────────────────────────────────── #
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=6)

        ttk.Button(btn_frame, text="Update Selected",
                   command=self.update_item).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Delete Selected",
                   command=self.delete_item).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Today vs Yesterday",
                   command=self.compare_spending).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Clear All",
                   command=self.clear_all).pack(side="left", padx=6)

        # ── Total label ──────────────────────────────────────────────── #
        self.total_label = ttk.Label(
            self.root, text="Total Expenses: $0.00",
            font=("Arial", 12, "bold"))
        self.total_label.pack(pady=8)

    # ------------------------------------------------------------------ #
    # CRUD — Add                                                           #
    # ------------------------------------------------------------------ #

    def add_item(self):
        """Validate inputs and append a new expense record."""
        cat     = self.cat_entry.get().strip()
        amt_str = self.amt_entry.get().strip()

        if not cat or not amt_str:
            messagebox.showwarning(
                "Missing Input", "Please fill in both Category and Amount.")
            return

        try:
            amount = float(amt_str)
        except ValueError:
            messagebox.showerror(
                "Invalid Amount", "Amount must be a number (e.g. 25.50).")
            return

        if amount <= 0:
            messagebox.showwarning(
                "Invalid Amount", "Amount must be greater than zero.")
            return

        # Use max(id)+1 to avoid duplicate IDs after deletions
        new_id = max((item["id"] for item in self.data), default=0) + 1

        self.data.append({
            "id":       new_id,
            "date":     datetime.datetime.now().strftime("%Y-%m-%d"),
            "category": cat,
            "amount":   round(amount, 2)
        })
        self.save_data()
        self.update_treeview()

        self.cat_entry.delete(0, tk.END)
        self.amt_entry.delete(0, tk.END)
        self.cat_entry.focus()

    # ------------------------------------------------------------------ #
    # CRUD — Update                                                        #
    # ------------------------------------------------------------------ #

    def update_item(self):
        """Update the selected record using the values in the input fields.

        Workflow: select a row → type new category & amount → click Update.
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(
                "No Selection", "Please select a record to update.")
            return

        new_category  = self.cat_entry.get().strip()
        new_amount_str = self.amt_entry.get().strip()

        if not new_category or not new_amount_str:
            messagebox.showwarning(
                "Missing Input",
                "Type the new Category and Amount in the fields above,\n"
                "then click Update Selected."
            )
            return

        try:
            new_amount = float(new_amount_str)
        except ValueError:
            messagebox.showerror(
                "Invalid Amount", "Amount must be a number (e.g. 25.50).")
            return

        if new_amount <= 0:
            messagebox.showwarning(
                "Invalid Amount", "Amount must be greater than zero.")
            return

        item_id = self.tree.item(selected[0])['values'][0]
        for exp in self.data:
            if exp['id'] == item_id:
                exp['category'] = new_category
                exp['amount']   = round(new_amount, 2)
                break

        self.save_data()
        self.update_treeview()
        messagebox.showinfo("Updated", "Record updated successfully.")

        self.cat_entry.delete(0, tk.END)
        self.amt_entry.delete(0, tk.END)

    # ------------------------------------------------------------------ #
    # CRUD — Delete                                                        #
    # ------------------------------------------------------------------ #

    def delete_item(self):
        """Delete the selected expense record (with confirmation)."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(
                "No Selection", "Please select a record to delete.")
            return

        vals = self.tree.item(selected[0])['values']
        if not messagebox.askyesno(
                "Confirm Delete",
                f"Delete record ID {vals[0]}  |  {vals[2]}  |  ${float(vals[3]):.2f}?"):
            return

        self.data = [i for i in self.data if i['id'] != vals[0]]
        self.save_data()
        self.update_treeview()

    def clear_all(self):
        """Delete every record after confirmation."""
        if not self.data:
            messagebox.showinfo("Empty", "The expense list is already empty.")
            return
        if messagebox.askyesno(
                "Confirm Clear All",
                "Delete ALL expense records?\nThis cannot be undone."):
            self.data = []
            self.save_data()
            self.update_treeview()

    # ------------------------------------------------------------------ #
    # Compare spending: today vs yesterday                                 #
    # ------------------------------------------------------------------ #

    def compare_spending(self):
        """Show a popup comparing today's total vs yesterday's total."""
        today     = datetime.date.today().isoformat()
        yesterday = (datetime.date.today() -
                     datetime.timedelta(days=1)).isoformat()

        today_sum     = sum(e['amount'] for e in self.data if e['date'] == today)
        yesterday_sum = sum(e['amount'] for e in self.data if e['date'] == yesterday)

        diff   = today_sum - yesterday_sum
        if diff > 0:
            status = f"${diff:.2f} MORE than yesterday"
        elif diff < 0:
            status = f"${abs(diff):.2f} LESS than yesterday"
        else:
            status = "the same as yesterday"

        messagebox.showinfo(
            "Today vs Yesterday",
            f"Today ({today}):        ${today_sum:.2f}\n"
            f"Yesterday ({yesterday}): ${yesterday_sum:.2f}\n\n"
            f"You spent {status}."
        )

    # ------------------------------------------------------------------ #
    # Income & Balance                                                     #
    # ------------------------------------------------------------------ #

    def calculate_balance(self):
        """Calculate remaining balance = monthly income - total expenses."""
        try:
            income = float(self.income_entry.get().strip())
        except ValueError:
            messagebox.showerror(
                "Invalid Income", "Please enter a valid number for income.")
            return

        total_spent = sum(e['amount'] for e in self.data)
        balance     = income - total_spent
        colour      = "green" if balance >= 0 else "red"
        self.balance_label.config(
            text=f"Balance: ${balance:.2f}", foreground=colour)

    # ------------------------------------------------------------------ #
    # Treeview refresh                                                     #
    # ------------------------------------------------------------------ #

    def update_treeview(self):
        """Repopulate the Treeview and update the running total."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        total = 0.0
        for item in self.data:
            self.tree.insert(
                "", "end",
                values=(
                    item["id"],
                    item["date"],
                    item["category"],
                    f"{item['amount']:.2f}"
                )
            )
            total += item["amount"]

        self.total_label.config(text=f"Total Expenses: ${total:.2f}")


# ------------------------------------------------------------------ #
# Entry point                                                          #
# ------------------------------------------------------------------ #

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
