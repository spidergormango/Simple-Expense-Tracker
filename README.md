1. Graphical Abstract
![Main Interface](https://via.placeholder.com/600x400.png?text=Upload+Your+App+Screenshot+Here)
*Figure 1: The Graphical User Interface (GUI) of the Personal Expense Tracker, showcasing the input area, expense list, and total balance display.*

---

2. Purpose of the Software
This software is a lightweight **Personal Expense Tracker** designed for undergraduate students to manage their daily finances efficiently. 

### Development Process: Agile Methodology
We adopted the **Agile Development Process** for this project. 
- **Why Agile?** It allows our 4-person team to develop a "Pilot Level" software quickly and perform iterative updates based on testing. This ensures the software remains functional and user-friendly within a short development cycle.
- **Goal**: To provide a simple, secure, and offline solution for tracking income and expenses using a local database (JSON).



3. Software Development Plan

### 3.1 Members (Roles & Responsibilities)
| Name | Role | Responsibilities | Contribution |
| :--- | :--- | :--- | :--- |
| [Your Name] | Project Manager (PM) | GitHub Repo management, Documentation, and QA. | 25% |
| [Member B] | Lead Developer | Core GUI development and CRUD logic implementation. | 25% |
| [Member C] | Algorithm Engineer | Data structure design (JSON) and Flowchart modeling. | 25% |
| [Member D] | Media Specialist | Video demo production and Graphical Abstract design. | 25% |

3.2 Development Schedule
| Phase | Task | Status |
| :--- | :--- | :--- |
| Phase 1 | Requirements analysis & UI Mockup | Completed |
| Phase 2 | Basic CRUD Logic Development (CLI) | Completed |
| Phase 3 | GUI Implementation (Tkinter) | In Progress |
| Phase 4 | Testing & Final Documentation | Pending |

3.3 Algorithm (Flowchart)
Our software follows an **Event-Driven Architecture**:
1. **Start**: Initialize the main window.
2. **Input**: User enters Category and Amount.
3. **Validation**: Check if inputs are valid (e.g., non-empty, numeric amount).
4. **Processing**: Write data to `expenses.json`.
5. **UI Update**: Refresh the Treeview list and recalculate the Total Expense.
6. **End**.

---

4. Environment & Declaration

4.1 System Requirements
- **Language**: Python 3.x
- **Libraries**: Tkinter (Built-in), JSON (Built-in), OS, Datetime.
- **Operating System**: Windows / macOS / Linux (Cross-platform).

4.2 Declaration
We hereby declare that:
1. The source code is originally developed by our team members.
2. All third-party libraries (Tkinter) used in this project are properly declared.
3. The software is provided as a pilot level demonstration for the COMP2116 course.
