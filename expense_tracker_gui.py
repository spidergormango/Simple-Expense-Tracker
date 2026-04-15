import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import datetime
from tkinter import messagebox, simpledialog

DATA_FILE = 'expenses.json'

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("個人財務收支管理工具 V2.0")
        self.root.geometry("600x500")
        
        # 初始化資料
        self.data = self.load_data()
        
        # UI 配置
        self.create_widgets()
        self.update_treeview()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_data(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
     # 1. Update Function (更新選中的記錄)
    def update_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Update Error", "Please select an item to update.")
            return
    
    # 獲取新數據 (範例使用彈窗，也可直接讀取 Entry 框)
        new_category = self.category_entry.get()
        new_amount = self.amount_entry.get()
    
        if new_category and new_amount:
            item_id = self.tree.item(selected_item)['values'][0]
            for exp in self.expenses:
                if exp['id'] == item_id:
                    exp['category'] = new_category
                    exp['amount'] = float(new_amount)
            self.save_data()
            self.refresh_tree()
            messagebox.showinfo("Success", "Record updated successfully.")

# 2. Compare Function (昨日 vs 今日)
    def compare_spending(self):
    today = datetime.date.today().isoformat()
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    
    today_sum = sum(e['amount'] for e in self.expenses if e['date'] == today)
    yesterday_sum = sum(e['amount'] for e in self.expenses if e['date'] == yesterday)
    
    diff = today_sum - yesterday_sum
    status = "more" if diff > 0 else "less"
    messagebox.showinfo("Comparison", f"Today: ${today_sum}\nYesterday: ${yesterday_sum}\nYou spent ${abs(diff)} {status} than yesterday.")

# 3. Income & Balance (計算剩餘預算)
    def calculate_balance(self):
        try:
            income = float(self.income_entry.get())
            total_spent = sum(e['amount'] for e in self.expenses)
            balance = income - total_spent
            self.balance_label.config(text=f"Balance: ${balance:.2f}", fg="green" if balance >= 0 else "red")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for income.")


    def create_widgets(self):
        # 輸入區塊
        input_frame = ttk.LabelFrame(self.root, text="新增開銷")
        input_frame.pack(pady=10, padx=10, fill="x")

        ttk.Label(input_frame, text="類別:").grid(row=0, column=0, padx=5, pady=5)
        self.cat_entry = ttk.Entry(input_frame)
        self.cat_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="金額:").grid(row=0, column=2, padx=5, pady=5)
        self.amt_entry = ttk.Entry(input_frame)
        self.amt_entry.grid(row=0, column=3, padx=5, pady=5)

        add_btn = ttk.Button(input_frame, text="新增紀錄", command=self.add_item)
        add_btn.grid(row=0, column=4, padx=5, pady=5)

        # 列表區塊
        list_frame = ttk.Frame(self.root)
        list_frame.pack(pady=10, padx=10, fill="both", expand=True)

        columns = ("id", "date", "category", "amount")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("date", text="日期")
        self.tree.heading("category", text="類別")
        self.tree.heading("amount", text="金額 ($)")
        self.tree.pack(side="left", fill="both", expand=True)

        # 功能按鈕
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="刪除選定紀錄", command=self.delete_item).pack(side="left", padx=5)
        
        self.total_label = ttk.Label(self.root, text="總支出: $0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_item(self):
        cat = self.cat_entry.get()
        amt = self.amt_entry.get()
        
        if not cat or not amt:
            messagebox.showwarning("警告", "請完整填寫類別與金額！")
            return
        
        try:
            new_item = {
                "id": len(self.data) + 1,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "category": cat,
                "amount": float(amt)
            }
            self.data.append(new_item)
            self.save_data()
            self.update_treeview()
            self.cat_entry.delete(0, tk.END)
            self.amt_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("錯誤", "金額必須是數字！")

    def update_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        total = 0
        for item in self.data:
            self.tree.insert("", "end", values=(item["id"], item["date"], item["category"], item["amount"]))
            total += item["amount"]
        self.total_label.config(text=f"總支出: ${total:.2f}")

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("警告", "請先選擇一筆紀錄！")
            return
        
        item_values = self.tree.item(selected[0])['values']
        self.data = [i for i in self.data if i['id'] != item_values[0]]
        self.save_data()
        self.update_treeview()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
