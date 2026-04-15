## Table of Contents

* [1. Graphical Abstract](#graphical-abstract)
* [2. Purpose of the Software](#purpose-of-the-software)
  * [Software Development Process](#software-development-process)
  * [Why Agile over Waterfall?](#why-agile-over-waterfall)
  * [Target Market & Possible Usage](#target-market--possible-usage)
* [3. Software Development Plan](#software-development-plan)
  * [Development Process](#development-process)
  * [Members (Roles & Responsibilities & Portion)](#members-roles--responsibilities--portion)
  * [Schedule](#schedule)
  * [Algorithm](#algorithm)
  * [Current Status](#current-status)
  * [Future Plan](#future-plan)
* [4. Environment](#environment)
* [5. How to Run](#how-to-run)
* [6. Demo](#demo)
* [7. Declaration](#declaration)

---

---# 💰 Personal Expense Tracker (GUI Version)

> A lightweight desktop CRUD application for recording and managing daily personal expenses, built with Python and Tkinter.

---

## 1. Graphical Abstract

<!-- Replace the path below with your actual screenshot once uploaded to GitHub -->
![Main Interface](./screenshots/main_interface.png)

*Figure 1: The main interface showing the transaction list, input fields, and running budget summary.*

---

## 2. Purpose of the Software

### Software Development Process

We implemented the **Agile Methodology** for this project. Development was split into short iterative sprints, with each sprint delivering a working, testable increment of the software. Team members reviewed progress at the end of each sprint and adjusted the next sprint's goals accordingly.

**Why Agile over Waterfall?**

| Criteria | Waterfall | Agile (Our Choice ✓) |
|---|---|---|
| Requirements clarity | Fixed upfront | Evolving & flexible |
| Team size | Large teams | Small teams (4 members) |
| Feedback cycle | End of project | Every sprint |
| Risk of wasted work | High | Low |

Because our team is small (4 members) and the requirements for a personal finance tool could evolve (e.g., we added GUI after initially planning CLI), Agile allowed us to adapt quickly without rewriting the entire plan.

### Target Market / Possible Usage

- **Students** tracking monthly allowances and daily spending.
- **Young professionals** who want a simple, offline-first budget tool without cloud dependency.
- **Anyone** who wants a lightweight alternative to complex spreadsheet-based budgeting.

---

## 3. Software Development Plan

### 3.1 Development Process

We followed a 3-sprint Agile cycle:

| Sprint | Goal | Deliverable |
|---|---|---|
| Sprint 1 | Core data layer | `expenses.json` CRUD + file I/O |
| Sprint 2 | GUI implementation | Tkinter window, Treeview, input forms |
| Sprint 3 | Polish & documentation | Error handling, README, demo video |

### 3.2 Members — Roles & Responsibilities

| GitHub Username | Role | Responsibilities | Contribution |
|---|---|---|---|
| `spidergormango` | Project Lead & Backend Dev | Architecture design, JSON data layer, `load_data` / `save_data` functions | 30% |
| `dengguoyao23-sketch` | Frontend Dev | Tkinter GUI layout, widget creation, Treeview display | 25% |
| `tangzhuoxuan06-sketch` | Logic & Integration | `add_item`, `delete_item` logic, input validation, error handling | 25% |
| `elvis060716-dev` | QA & Documentation | Testing, bug reports, README writing, demo video | 20% |

### 3.3 Schedule (Gantt Overview)

```
Week 1  | [=====] Requirements & design
Week 2  | [=====] Sprint 1 — Data layer (JSON I/O)
Week 3  | [=====] Sprint 2 — GUI implementation
Week 4  | [=====] Sprint 3 — Testing & polish
Week 5  | [=====] Documentation & demo video
```

### 3.4 Algorithm

The application follows a simple event-driven loop. Below is the main algorithm flowchart:

<!-- Replace with your exported flowchart image -->
![Algorithm Flowchart](./screenshots/algorithm_flowchart.png)

*Figure 2: Algorithm flowchart covering the Add, Delete, and View Total operations.*

**Core logic summary:**

1. **Startup** — Load `expenses.json` if it exists; otherwise initialise an empty list.
2. **Render** — Build the Tkinter window, Treeview table, and total label.
3. **Add Expense**
   - Validate that both `category` and `amount` fields are non-empty.
   - Validate that `amount` is a valid number (float).
   - Append a new record `{ id, date, category, amount }` to the list.
   - Persist to `expenses.json` and refresh the Treeview.
4. **Delete Expense**
   - Check that a row is selected in the Treeview.
   - Filter out the record whose `id` matches the selected row.
   - Persist to `expenses.json` and refresh the Treeview.
5. **View Total** — Recalculate the sum of all `amount` values and update the label on every Treeview refresh.
6. **Loop** — Return to idle state and await the next user action.

### 3.5 Current Status

| Feature | Status |
|---|---|
| Add expense (category + amount) | ✅ Complete |
| Delete selected expense | ✅ Complete |
| View running total | ✅ Complete |
| Persistent JSON storage | ✅ Complete |
| Input validation & error dialogs | ✅ Complete |
| GUI (Tkinter) | ✅ Complete |

### 3.6 Future Plan

- [ ] **Edit expense** — Allow updating category or amount of an existing record without deleting and re-adding.
- [ ] **Category filter** — Filter the Treeview by category (e.g., show only "Food" expenses).
- [ ] **Monthly budget limit** — Set a monthly spending cap and trigger a visual alert when it is exceeded.
- [ ] **Data export** — Export expenses to CSV for use in Excel or Google Sheets.
- [ ] **Charts & visualisations** — Pie chart or bar chart breakdown of spending by category using `matplotlib`.
- [ ] **Dark mode UI** — Toggle between light and dark themes.

---

## 4. Demo

▶️ **Watch the demo on YouTube:** [https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

*(Replace the URL above with your actual YouTube link before submission.)*

---

## 5. Environment

### Requirements

| Item | Requirement |
|---|---|
| **Programming Language** | Python 3.8 or above |
| **GUI Library** | `tkinter` (built into Python standard library) |
| **Data Storage** | `json` (built into Python standard library) |
| **OS** | Windows 10/11, macOS 12+, or Ubuntu 20.04+ |
| **Minimum RAM** | 256 MB |
| **Minimum Storage** | 10 MB |

### How to Run

```bash
# 1. Clone the repository
git clone https://github.com/spidergormango/Simple-Expense-Tracker.git
cd Simple-Expense-Tracker

# 2. (No extra packages needed — uses Python standard library only)

# 3. Run the application
python expense_tracker_gui.py
```

> **Note:** On some Linux distributions, Tkinter must be installed separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 6. Declaration

This software was developed entirely by the project team members listed above as original work for COMP2116: Software Engineering at Macao Polytechnic University.

**Third-party libraries and open-source resources used:**

| Resource | Purpose | License |
|---|---|---|
| `tkinter` | GUI framework | Python Software Foundation License (PSF) — part of Python standard library |
| `json` | Data serialisation | Python Software Foundation License (PSF) — part of Python standard library |
| `datetime` | Timestamping records | Python Software Foundation License (PSF) — part of Python standard library |
| `os` | File existence checking | Python Software Foundation License (PSF) — part of Python standard library |

No external paid assets, proprietary code, or unlicensed open-source code was used in this project.

---

## 7. References

- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Atlassian. *What is Agile?* https://www.atlassian.com/agile
- GitHub Docs. *About README files*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

---

*COMP2116: Software Engineering — Group Final Project | Macao Polytechnic University*
