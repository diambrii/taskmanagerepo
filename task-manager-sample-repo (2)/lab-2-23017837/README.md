# COMP 441 — Lab 2: Static Analysis, Metrics, Linting & AI Code Review

**Student ID:** 23017837  
**Project:** Task Manager Sample Repository  
**Repository:** https://github.com/diambrii/taskmanagerepo

## Lab overview

This lab assessed the Task Manager Python application using rule-based linting, code-complexity metrics and AI-assisted code review. Three Pylint findings were corrected, and the results were compared before and after the changes.

## Tools used

| Tool | Version or purpose |
| --- | --- |
| Python | 3.14.7 |
| Pylint | 4.1.3 |
| Radon | 6.0.1 |
| Pytest | 9.1.1 |
| ChatGPT | AI-assisted review of two code snippets |

## Work completed and results

- Ran Pylint on the `app` package and saved the original and updated reports.
- Reviewed 12 initial Pylint findings and assessed 10 of them by severity and estimated fix effort.
- Used Radon to measure cyclomatic complexity and maintainability. All measured functions received complexity grade **A**.
- Recorded maintainability indices of **72.27** for `cli.py`, **72.97** for `storage.py` and **45.51** for `tasks.py` (all grade **A**).
- Corrected three reported issues in `app/tasks.py`:
  - **W0102:** Replaced the mutable default `tags=[]` with `tags=None`, creating a new list when necessary.
  - **R1732:** Used `with open(..., encoding="utf-8")` to ensure the task file is closed properly.
  - **R1710:** Added an explicit `return None` to `find_task_by_title()` when no matching task is found.
- Confirmed that all three warning codes were absent from the updated Pylint report.
- Improved the Pylint score from **8.33/10** to **8.93/10** (an increase of **0.60**).
- Compared Pylint findings with ChatGPT's review of the original `add_task()` and `load_tasks()` code snippets.
- Re-ran the existing test suite: **6 tests collected, 4 passed and 2 failed**. The two failures were the pre-existing pending-task and empty-list average-priority defects; no additional test failures were introduced by the three corrections.

## Submission files

| File | Contents |
| --- | --- |
| `COMP441_Lab2_Report_23017837.docx` | Analysis, metrics, 10-finding triage, AI comparison, corrections and reflection |
| `README.md` | Summary of the lab activities and results |
| `lint_before.txt` | Original Pylint output |
| `lint_after.txt` | Pylint output after the corrections |
| `complexity.txt` | Radon cyclomatic-complexity output |
| `maintainability.txt` | Radon maintainability-index output |
| `fixes.diff` | Git diff showing the three source-code corrections |

The corrected application source is maintained in `app/tasks.py` within the same repository.
