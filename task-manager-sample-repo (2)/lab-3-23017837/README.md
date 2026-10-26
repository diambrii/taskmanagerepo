# COMP 441 — Lab 3: Dynamic Analysis and Test Design Techniques

**Student ID:** 23017837  
**Project:** Task Manager sample repository  
**Function tested:** `calculate_discount(price, is_premium)` in `app/tasks.py`

## Objective

Apply equivalence partitioning and boundary value analysis to the discount function, execute Pytest cases, and compare the coverage of two test sets.

## Test design

The function gives premium customers a 20% discount and leaves the price unchanged for regular customers. The test-design tables in the report cover zero, positive whole-number and decimal prices, membership status, and exploratory invalid inputs. Zero is treated as the assumed minimum valid price because the project does not specify input limits.

## Testing and results

| Test set or activity | Result |
|---|---|
| AI-generated discount tests (`test_discount_cases.py`) | 10 passed, 0 failed |
| Comparison tests executed and checked in VS Code (`test_discount_comparison.py`) | 10 passed, 0 failed |
| Negative-price observation: `calculate_discount(-0.01, True)` | Returned `-0.008` |
| Non-Boolean status observation: `calculate_discount(100, "yes")` | Returned `100` |

The two executable suites were run using Pytest.

## Comparison and findings

The test sets overlap on zero and small-positive-price cases for both premium and regular customers. A separate review of six selected boundary combinations found four in the original set (**4/6 = 66.7%**). The two negative-price combinations were absent from that set.

The application accepts the exploratory invalid values used above without validation. Because the provided project specification does not define invalid-input handling, these are recorded as observed behaviour rather than confirmed specification defects.

## Submission files

- `COMP441_Lab3_Updated.docx` — test specification, equivalence-partition and boundary-value tables, test design, results, comparison, and reflection.
- `test_discount_cases.py` — original executable test cases.
- `test_discount_comparison.py` — executable comparison test cases.
- `test_results.txt` — output from the original suite.
- `comparison_results.txt` — output from the comparison suite.
- `invalid_input_results.txt` — exploratory invalid-input observations.
- `README.md` — summary of the Lab 3 work and evidence.

## Run tests

From the Task Manager project root:

```cmd
python -m pytest lab-3-23017837/test_discount_cases.py -v
python -m pytest lab-3-23017837/test_discount_comparison.py -v
```
