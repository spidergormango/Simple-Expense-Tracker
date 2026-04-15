# 💰 Personal Expense Tracker (GUI Version)

> A lightweight desktop application for recording, managing, and analysing daily personal expenses — built with Python and Tkinter, with zero external dependencies.

---

## ## Table of Contents

* [1. Graphical Abstract](#1-graphical-abstract)
* [2. Purpose of the Software](#2-purpose-of-the-software)
  * [Software Development Process](#software-development-process)
  * [Why Agile over Waterfall?](#why-agile-over-waterfall)
  * [Target Market / Possible Usage](#target-market--possible-usage)
* [3. Software Development Plan](#3-software-development-plan)
  * [3.1 Development Process](#31-development-process)
  * [3.2 Members — Roles & Responsibilities](#32-members--roles--responsibilities)
  * [3.3 Schedule](#33-schedule)
  * [3.4 Algorithm](#34-algorithm)
  * [3.5 Current Status](#35-current-status)
  * [3.6 Future Plan](#36-future-plan)
* [4. Environment](#4-environment)
* [5. How to Run](#5-how-to-run)
* [6. Declaration](#6-declaration)
* [7. References](#7-references)

---

## ## 1. Graphical Abstract

![Main Interface](./screenshots/main_interface.png)
*Figure 1: The main interface showing the expense list, income/balance calculator, and advanced analysis tools.*

---

## ## 2. Purpose of the Software

### Software Development Process
We implemented the **Agile Methodology** for this project. Development was split into short iterative sprints, allowing us to add features like "Income Tracking" and "Search" after the core CRUD logic was validated.

### Why Agile over Waterfall?
| Criteria | Waterfall | Agile (Our Choice ✓) |
|---|---|---|
| **Flexibility** | Fixed upfront | Evolving & flexible |
| **Team Size** | Large teams | Small teams (4 members) |
| **Risk Management** | High | Low (early testing) |

---

## ## 3. Software Development Plan

### 3.1 Development Process
Our team followed a 4-stage cycle: **Requirement Analysis** → **GUI Prototyping** → **Core Logic Coding** → **Integration & Testing**.

### 3.2 Members — Roles & Responsibilities
| Name | Role | Responsibilities | Portion |
| :--- | :--- | :--- | :--- |
| Member A | Project Manager | Documentation & GitHub Management | 25% |
| Member B | Lead Developer | Core Python Logic & JSON Data Layer | 25% |
| Member C | UI Designer | Tkinter GUI Layout & UX Optimization | 25% |
| Member D | QA Engineer | Testing, Debugging & Comparison Logic | 25% |

### 3.3 Schedule
- **Week 1**: UI Design and Basic Add/Delete functions.
- **Week 2**: Implementation of Update, Search, and JSON persistence.
- **Week 3**: Final integration of Comparison and Monthly Summary features.

### 3.4 Algorithm
The software operates based on the following logical flow:
1. **Data Initialization**: On startup, the program calls `load_data()` to parse `expenses.json`. If the file is missing or corrupt, it initializes an empty list.
2. **ID Generation**: For every new record, the algorithm finds the `max(id)` in the existing list and adds 1 to ensure a unique primary key.
3. **Validation**: Before saving, it checks if the 'Amount' can be converted to a float and if the 'Category' is non-empty.
4. **Financial Calculation**:
   - **Balance**: `Income - Sum(All Expenses)`.
   - **Comparison**: Fetches sums filtered by `Date == Today` and `Date == Yesterday`.
   - **Summary**: Uses a Dictionary to aggregate totals by Category and identifies the `max()` value.
5. **Persistence**: Every change (Add/Update/Delete) triggers `save_data()` to sync the local list with the JSON file.

### 3.5 Current Status
All core and advanced functions are **fully operational**:
- ✅ **Full CRUD**: Add, View, Update, and Delete individual/all records.
- ✅ **Search/Filter**: Filter records by category keyword.
- ✅ **Financial Analysis**: Real-time balance calculation based on income.
- ✅ **Comparative Insights**: Daily spending comparison and monthly top-category summary.

### 3.6 Future Plan
- [ ] **Data Visualization**: Adding Matplotlib for pie charts and bar graphs.
- [ ] **Export Function**: Exporting data to CSV or Excel for external reporting.

---

## ## 4. Environment
- **Programming Language**: Python 3.10+
- **Libraries (Standard Only)**:
  - `tkinter`: GUI framework.
  - `json`: Data serialization.
  - `os`: File path management.
  - `datetime`: Time stamping and comparisons.

---

## ## 5. How to Run
```bash
# 1. Clone the repository
git clone [Your Repository URL]

# 2. Run the application
python expense_tracker_gui.py
