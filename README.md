# Personal Expense Tracker (GUI Version)

---

## 1. Graphical Abstract
![Main Interface](https://raw.githubusercontent.com/[你的GitHub用戶名]/[倉庫名]/main/screenshot.png)
*Figure 1: The main interface of the application showing the transaction list and budget summary.*

---

## 2. Purpose of the Software
### Software Development Process
[cite_start]We implemented the **Agile Methodology** for this project[cite: 46]. 

### Why Agile over Waterfall?
- [cite_start]**Iterative Development**: Agile allows our team to build a "pilot level" functional prototype quickly and refine the UI based on internal testing[cite: 32, 47].
- [cite_start]**Flexibility**: Given the short development cycle, Agile helps us manage tasks across 4 members more efficiently compared to the rigid phases of Waterfall[cite: 47].

### Target Market & Possible Usage
[cite_start]This software is designed for **university students** who need a simple, offline, and secure way to track their daily expenses (e.g., food, transport, academic materials) without complex banking integration[cite: 48].

---

## 3. Software Development Plan
### Development Process
Our team followed a 3-week sprint cycle: Requirement Analysis -> UI Design -> Core Coding -> Testing.

### Members (Roles & Responsibilities & Portion)
| Name | Role | Responsibilities | Portion |
| :--- | :--- | :--- | :--- |
| [Student A] | Project Manager | GitHub Management & Documentation | 25% |
| [Student B] | Lead Developer | Core Python Logic & JSON Database | 25% |
| [Student C] | UI/UX Designer | Tkinter GUI Design & Graphical Abstract | 25% |
| [Student D] | QA & Media | Testing & Video Demo Production | 25% |

### Schedule
- [cite_start]**Week 1**: Environment setup and initial GUI mockup[cite: 52].
- [cite_start]**Week 2**: Implementation of CRUD logic and JSON integration[cite: 52].
- [cite_start]**Week 3**: Final debugging, documentation, and video recording[cite: 52].

### Algorithm
1. **Initialize**: Load previous data from `expenses.json`.
2. **Input**: User enters category (String) and amount (Float).
3. [cite_start]**Validation**: Check if inputs are valid and non-empty[cite: 53].
4. [cite_start]**Processing**: Append data to local list and update total sum[cite: 53].
5. [cite_start]**Output**: Refresh the Treeview display and save to JSON[cite: 53].

### Current Status
[cite_start]The software has reached the **Pilot Level**[cite: 32, 54]. All core functions (Add, Delete, View, Totaling) are fully operational.

### Future Plan
- Add data visualization (Pie charts for spending categories).
- [cite_start]Implement a password-protected login system for privacy[cite: 55].

---

## 4. Environment
- [cite_start]**Programming Language**: Python 3.10 or above[cite: 62].
- **Operating System**: Cross-platform (Windows, macOS, Linux).
- [cite_start]**Libraries**: Tkinter (Standard Library), JSON, OS, Datetime[cite: 62].
- [cite_start]**Hardware**: Minimum 4GB RAM and 100MB disk space[cite: 62].

---

## 5. How to Run
1. Ensure you have **Python 3** installed on your computer.
2. Download all files from this GitHub repository.
3. Open your terminal or command prompt.
4. Navigate to the project folder and run:
   ```bash
   python expense_tracker_gui.py
