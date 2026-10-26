# COMP 441 — Lab 1: Environment Setup & Manual Defect Hunting

## Project

**Application:** Python Task Manager sample application  
**Module:** COMP 441 — Software Analysis and Testing  
**Lab:** 1 — Environment Setup & Manual Defect Hunting

## Environment

The project was opened in Visual Studio Code, and its Python dependencies were verified using `requirements.txt`.

| Tool | Version |
| --- | --- |
| Git | 2.53.0.windows.2 |
| Python | 3.14.7 |
| pytest | 9.1.1 |
| AI assistant | ChatGPT |

## Work Completed

- Inspected the application source files: `app/tasks.py`, `app/storage.py`, and `app/cli.py`.
- Reviewed the code manually and recorded **10 suspected defects** in the Lab 1 report, including their file locations, descriptions, and severity assessments.
- Used ChatGPT to discuss code behaviour and review the cause of failing tests.
- Ran the application from the project root using `python -m app.cli`. It reported **0 loaded tasks** and **0 pending tasks**.
- Executed the existing test suite using `python -m pytest -v` and recorded the baseline results.

## Baseline Test Results

| Result | Count |
| --- | ---: |
| Tests collected | 6 |
| Passed | 4 |
| Failed | 2 |

The two failing tests were:

1. `test_get_pending_tasks_includes_first_task` — the pending-task loop begins at index 1 and omits the first task.
2. `test_average_priority_of_empty_list` — calculating the average for an empty list raises `ZeroDivisionError`.

## Submission Contents

The accompanying **Lab 1 report** contains the defect log, tool-version and application-execution screenshots, baseline test evidence, and discussion of automated versus manual defect detection.

The source code was left unchanged during Lab 1 to preserve the original defects for subsequent analysis and testing.
