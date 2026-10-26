# COMP 441 — Lab 3: Dynamic Analysis & Test Design Techniques

**Student ID:** 23017837  
**Project:** Task Manager sample repository  
**Target function:** `app.tasks.calculate_discount()`

## Overview

This lab investigated discount-calculation behaviour through equivalence partitioning and boundary-value analysis. An AI-generated test suite was evaluated alongside a separate comparison suite, and invalid-input behaviour was explored.

## Test results

- **AI-generated suite (`test_discount_cases.py`):** 10 passed, 0 failed.
- **Comparison suite (`test_discount_comparison.py`):** 10 passed, 0 failed.
- **Overlap:** 4 identical input combinations; 6 different combinations in each ten-case set.
- **Negative-price observation:** `calculate_discount(-0.01, True)` returned `-0.008`.
- **Non-Boolean status observation:** `calculate_discount(100, "yes")` returned `100`.

The project documentation does not specify a maximum price or a required response to invalid inputs. These observations are therefore reported as possible validation gaps rather than confirmed specification violations.

## Submitted files

- `COMP441_Lab3_Report_23017837.docx` — equivalence-partition and boundary-value tables, test cases, results, comparison and discussion.
- `test_discount_cases.py` — ten AI-generated test cases.
- `test_discount_comparison.py` — ten comparison test cases reviewed and executed by the student with assistant support.
- `test_results.txt` — results for the first suite.
- `comparison_results.txt` — results for the second suite.
- `invalid_input_results.txt` — results of exploratory invalid-input checks.

## Running the tests

From the project root:

```cmd
python -m pytest COMP441_Lab3_23017837/test_discount_cases.py -v
python -m pytest COMP441_Lab3_23017837/test_discount_comparison.py -v
```
