# COMP 441 - Lab 5: Test Automation Framework & Self-Healing Locators

**Student number:** 23017837

## Aim
I developed a Selenium Page Object Model (POM) for the Add/Remove Elements page of the local *The Internet* application and evaluated Healenium's behaviour when a working element locator changed.

## Test environment
- Python 3.14.7; Pytest 9.1.1; Selenium with Microsoft Edge (ordinary runs)
- Docker-hosted *The Internet* at `http://localhost:5000/add_remove_elements/`
- Healenium-Proxy at `http://localhost:8085` with a Chrome node inside Docker
- Remote browser website URL: `http://host.docker.internal:5000/add_remove_elements/`

## Files
- `add_remove_page.py`: Page Object class with reusable locators and page actions.
- `test_data.json`: five external data-driven scenarios (required by the laboratory manual).
- `test_add_remove.py`: ordinary Selenium/Pytest version reading `test_data.json`.
- `test_add_remove_healenium.py`: proxy-based version reading the same JSON cases.
- `baseline_results.txt`: normal Selenium baseline output.
- `healenium_baseline_results.txt`: Healenium baseline output.
- `locator_change.diff`: intentional DOM change evidence.
- `broken_locator_results.txt`: ordinary Selenium results after changing the locator.
- `healenium_after_change_results.txt`: Healenium results after the change.
- `healenium_proxy_logs.txt`: recorded healing decisions and selected locators.
- `diagnose_healing.py`, `healing_diagnostic_results.txt`: focused repeated-click diagnostic.
- `COMP441_Lab5_Report_23017837.docx`: first-person report, result tables, reflection and embedded evidence screenshots.

## Test scenarios
| ID | Add | Delete | Expected remaining |
| --- | ---: | ---: | ---: |
| TC01_add_one | 1 | 0 | 1 |
| TC02_add_two_delete_one | 2 | 1 | 1 |
| TC03_delete_all | 3 | 3 | 0 |
| TC04_add_five_delete_two | 5 | 2 | 3 |
| TC05_add_one_delete_one | 1 | 1 | 0 |

## Commands
From the repository root (with the local website running):

```cmd
python -m pytest lab-5-23017837\test_add_remove.py -v
python -m pytest lab-5-23017837\test_add_remove_healenium.py -v
```

To check that the revised scripts collect the five JSON cases without executing them:

```cmd
python -m pytest lab-5-23017837\test_add_remove.py --collect-only -q
python -m pytest lab-5-23017837\test_add_remove_healenium.py --collect-only -q
```

## Experiment and observed results
1. The original UI: all five ordinary Selenium tests passed and all five Healenium-proxy tests passed.
2. I changed the Add Element button from `onclick="addElement()"` to `id="add-element-v2" class="add-button-v2" onclick="addElement();"` without changing its intended behaviour.
3. Ordinary Selenium after the change: five test setup errors (`TimeoutException`) because its old CSS locator no longer matched.
4. Healenium after the change: two tests passed and three failed functional assertions, an end-to-end pass rate of **40%**.
5. The healing dashboard recorded `button#add-element-v2` as a candidate for the broken locator. Its displayed confidence scores included **0.74** and **0.70**.
6. A five-attempt diagnostic selected the intended Add Element button on attempts 1, 3 and 5, but selected a Delete button on attempts 2 and 4. This is **3/5 = 60% correct element selection** in that specific diagnostic.

The 40% test pass rate and 60% diagnostic element-selection rate measure different things; neither should be described as the overall accuracy of all Healenium recovery attempts.

## Reflection
I found that Healenium could recover a locator after a small HTML change, but it could also choose a visually similar element with a different function. Small changes to an ID or attribute may be healed successfully when a target is unique. Ambiguous buttons, major UI redesigns and changes to application behaviour still require functional assertions and human review.

## Submission note
The original experiment results were recorded before I externalised the same five scenario values to JSON. The supplied test files use external JSON to satisfy the lab's data-file requirement. I will run the collection check after replacing the local test scripts; the archived evidence remains the record of the executed experiments. I will not describe the JSON-based revision as re-executed until it has been run.
