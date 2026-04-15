# 💰 Personal Expense Tracker (GUI Version)
## 📑 Table of Contents

* [1. Graphical Abstract](#1-graphical-abstract)
* [2. Purpose of the Software](#2-purpose-of-the-software)
    * [Software Development Process](#software-development-process)
    * [Target Market / Possible Usage](#target-market--possible-usage)
* [3. Software Development Plan](#3-software-development-plan)
    * [3.1 Development Process](#31-development-process)
    * [3.2 Members — Roles & Responsibilities](#32-members--roles--responsibilities)
    * [3.3 Schedule (Gantt Overview)](#33-schedule-gantt-overview)
    * [3.4 Algorithm](#34-algorithm)
    * [3.5 Current Status](#35-current-status)
    * [3.6 Future Plan](#36-future-plan)
* [4. Demo](#4-demo)
* [5. Environment](#5-environment)
    * [Requirements](#requirements)
    * [How to Run](#how-to-run)
* [6. Declaration](#6-declaration)
* [7. References](#7-references)

---

> A lightweight desktop application for recording, managing, and analysing daily personal expenses — built with Python and Tkinter, with zero external dependencies.

---

## 1. Graphical Abstract

<!-- After taking your screenshot, upload it to GitHub and update this path -->
![Main Interface](./screenshots/main_interface.png)

*Figure 1: The main interface showing the expense list, income/balance calculator, and action buttons.*

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
| Ability to add features mid-project | None | High |

Because our team is small (4 members) and requirements evolved during development (e.g., adding Income/Balance and Compare features after the initial CRUD release), Agile let us adapt quickly without rewriting the entire project plan.

### Target Market / Possible Usage

- **Students** tracking monthly allowances and daily spending habits.
- **Young professionals** who want a simple, offline-first, zero-signup budget tool.
- **Anyone** who wants a lightweight alternative to complex cloud-based budgeting apps.

---

## 3. Software Development Plan

### 3.1 Development Process

We followed a 3-sprint Agile cycle:

| Sprint | Goal | Deliverable |
|---|---|---|
| Sprint 1 | Core data layer | `expenses.json` CRUD, file I/O, JSON schema |
| Sprint 2 | GUI + advanced features | Tkinter window, Treeview, Update, Compare, Balance |
| Sprint 3 | Polish & documentation | Error handling, scrollbar, README, demo video |

### 3.2 Members — Roles & Responsibilities

| GitHub Username | Role | Responsibilities | Contribution |
|---|---|---|---|
| `spidergormango` | Project Lead & Backend Dev | Architecture design, JSON data layer, `load_data` / `save_data`, ID management | 25% |
| `dengguoyao23-sketch` | Frontend Dev | Tkinter GUI layout, Treeview, Income/Balance UI panel | 25% |
| `tangzhuoxuan06-sketch` | Logic & Integration | `add_item`, `update_item`, `delete_item`, `compare_spending`, input validation | 25% |
| `elvis060716-dev` | QA & Documentation | Testing, bug reports, `clear_all`, README writing, demo video | 25% |

### 3.3 Schedule (Gantt Overview)

```
Week 1  | [=====] Requirements gathering & system design
Week 2  | [=====] Sprint 1 — Data layer (JSON I/O, CRUD skeleton)
Week 3  | [=====] Sprint 2 — Full GUI, Update, Compare, Balance features
Week 4  | [=====] Sprint 3 — Testing, bug fixing, error handling
Week 5  | [=====] Documentation, README, demo video recording
```

### 3.4 Algorithm

The application follows an event-driven loop. The diagram below shows the full algorithm covering all five operations.

<!-- Upload your exported flowchart image to GitHub and update this path -->
![Algorithm Flowchart](./screenshots/algorithm_flowchart.png)

*Figure 2: Algorithm flowchart — Add, Update, Delete, Compare, and Balance operations.*

**Core logic summary:**

1. **Startup** — Load `expenses.json` if it exists; otherwise initialise an empty list. Render the main window.
2. **Add Expense**
   - Validate `category` (non-empty) and `amount` (positive number).
   - Assign `id = max(existing ids) + 1` to prevent duplicate IDs after deletions.
   - Append `{ id, date, category, amount }`, save to JSON, refresh Treeview.
3. **Update Expense**
   - User selects a row, types new values in the input fields, clicks Update.
   - Locate the record by `id`, overwrite `category` and `amount`, save and refresh.
4. **Delete Expense**
   - Prompt confirmation, filter out the record by `id`, save and refresh.
5. **Compare Spending (Today vs Yesterday)**
   - Aggregate today's and yesterday's totals from the data list.
   - Display the difference with a clear more/less/same message.
6. **Income & Balance**
   - Read the monthly income input, subtract total expenses, display balance in green (positive) or red (negative).
7. **Loop** — Return to idle state and await the next user action.

### 3.5 Current Status

| Feature | Status |
|---|---|
| Add expense (category + amount) | ✅ Complete |
| Update selected expense | ✅ Complete |
| Delete selected expense | ✅ Complete |
| Clear all expenses | ✅ Complete |
| View running total | ✅ Complete |
| Persistent JSON storage | ✅ Complete |
| Income & balance calculator | ✅ Complete |
| Compare today vs yesterday | ✅ Complete |
| Input validation & error dialogs | ✅ Complete |
| Scrollable expense list | ✅ Complete |
| Enter-key form submission | ✅ Complete |

### 3.6 Future Plan

- [ ] **Category filter** — Filter the Treeview to show only expenses in a chosen category.
- [ ] **Monthly budget limit** — Set a cap and trigger a visual alert when it is exceeded.
- [ ] **Data export** — Export the expense list to CSV for use in Excel or Google Sheets.
- [ ] **Charts & visualisations** — Pie chart or bar chart of spending by category using `matplotlib`.
- [ ] **Date range filter** — View expenses for a custom date range (e.g., "this week" or "last 30 days").
- [ ] **Dark mode UI** — Toggle between light and dark themes.

---

## 4. Demo

▶️ **Watch the demo on YouTube:** [https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

*(Replace the URL above with your actual YouTube link before submission.)*

**The demo video covers:**
- How to start and run the software
- Adding multiple expense records
- Updating an existing record
- Deleting a record
- Using the Income & Balance calculator
- Comparing today vs yesterday's spending
- Code walkthrough and team role explanation

---

## 5. Environment

### Requirements

| Item | Requirement |
|---|---|
| **Programming Language** | Python 3.8 or above |
| **GUI Library** | `tkinter` (Python standard library — no install needed) |
| **Data Storage** | `json` (Python standard library) |
| **Other modules used** | `os`, `datetime` (Python standard library) |
| **External packages** | None — zero dependencies |
| **OS** | Windows 10/11, macOS 12+, or Ubuntu 20.04+ |
| **Minimum RAM** | 256 MB |
| **Minimum Storage** | 10 MB |

### How to Run

```bash
# 1. Clone the repository
git clone https://github.com/spidergormango/Simple-Expense-Tracker.git
cd Simple-Expense-Tracker

# 2. No extra packages required — uses Python standard library only

# 3. Run the application
python expense_tracker_gui.py
```

> **Linux note:** On some Linux distributions, Tkinter must be installed separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 6. Declaration

This software was developed entirely by the four project team members listed above as original work for **COMP2116: Software Engineering** at Macao Polytechnic University.

**Third-party libraries and open-source resources used:**

| Resource | Purpose | License |
|---|---|---|
| `tkinter` | GUI framework | PSF License — Python standard library |
| `json` | Data serialisation | PSF License — Python standard library |
| `datetime` | Timestamping and date comparison | PSF License — Python standard library |
| `os` | File existence checking | PSF License — Python standard library |

No external paid assets, proprietary code, or unlicensed open-source packages were used in this project.

---

## 7. References

- Python Software Foundation. *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html
- Atlassian. *What is Agile?* https://www.atlassian.com/agile
- GitHub Docs. *About README files*. https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

---

*COMP2116: Software Engineering — Group Final Project | Macao Polytechnic University*
