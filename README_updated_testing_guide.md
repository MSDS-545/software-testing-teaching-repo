# Software Testing Teaching Repository

A classroom repository for teaching **unit testing, integration testing, acceptance testing, test-driven development (TDD), AI-assisted testing, and code coverage** across Python and JavaScript web stacks.

The examples are intentionally small. The goal is to help students see **what is being tested, which components participate in the test, and why a test is classified as unit, integration, or acceptance testing**.

---

## 1. Repository Learning Map

| Folder | Technology | What the folder demonstrates | Test levels |
|---|---|---|---|
| `python_examples/core_unit/` | Python | Small Python functions tested independently | **Unit** |
| `python_examples/flask_app/` | Flask | Flask application behavior, API interactions, and user-facing requirements | **Unit, Integration, Acceptance** |
| `python_examples/fastapi_app/` | FastAPI | FastAPI application logic and API endpoint behavior | **Unit, Integration, Acceptance** |
| `python_examples/flask_fastapi_shared/` | Flask + FastAPI | Multiple frameworks using shared domain/application behavior | **Integration / Contract consistency** |
| `python_examples/streamlit_app/` | Streamlit | Testable Python logic plus Streamlit UI behavior | **Unit, Acceptance** |
| `python_examples/streamlit_fastapi/` | Streamlit + FastAPI | Streamlit UI communicating with a FastAPI service | **Unit, Integration, Acceptance** |
| `tdd_lab/` | Python | Red → Green → Refactor workflow | **TDD / Unit** |
| `ai_testing/` | Python + AI-assisted workflow | Generating, reviewing, and improving tests with AI assistance | **Test design activity** |
| `node_istanbul/` | Node.js + Express | JavaScript testing and Istanbul/NYC coverage | **Unit, Integration, Acceptance** |
| `.github/workflows/` | GitHub Actions | Automatic execution of tests in CI | **Continuous Integration** |

---

## 2. Understanding the Test Levels

### Unit Testing

A **unit test** checks one small piece of application behavior in isolation.

Examples include:

- testing one Python function;
- testing validation logic;
- testing a calculation;
- testing an individual JavaScript function;
- testing edge cases with parametrized input.

The main question is:

> **Does this individual unit of code work correctly?**

Run only tests marked `unit`:

```bash
python -m pytest -m unit -v
```

---

### Integration Testing

An **integration test** verifies that multiple application components work together correctly.

Examples include:

- a FastAPI route working with application logic;
- a Flask route returning the expected API response;
- a Streamlit client correctly communicating with FastAPI;
- multiple services agreeing on a shared response contract.

The main question is:

> **Do these components work correctly when connected?**

Run only tests marked `integration`:

```bash
python -m pytest -m integration -v
```

---

### Acceptance Testing

An **acceptance test** checks whether the application satisfies an observable user or stakeholder requirement.

Examples include:

- a user enters a name and receives the expected greeting;
- a Streamlit interface displays the expected result;
- an HTTP request produces the behavior required by the application specification.

Acceptance tests may be written using **Given / When / Then**:

```text
Given the application is available
When the user performs an action
Then the expected behavior should occur
```

The main question is:

> **Does the application behave the way the user expects?**

Run only tests marked `acceptance`:

```bash
python -m pytest -m acceptance -v
```

---

## 3. Python Examples

### `python_examples/core_unit/`

**Purpose:** Introduces unit testing without the additional complexity of a web framework.

Students should use this folder first.

The application/source files contain small Python behaviors. The test files exercise those behaviors independently.

**Primary test type:** Unit testing.

Concepts demonstrated include:

- assertions;
- expected versus actual results;
- normal cases;
- edge cases;
- parametrized tests.

Run:

```bash
python -m pytest python_examples/core_unit -v
```

Or run all tests marked as unit tests:

```bash
python -m pytest -m unit -v
```

---

### `python_examples/flask_app/`

**Purpose:** Demonstrates how testing changes when application behavior is exposed through Flask routes.

The folder contains the Flask application code and tests that examine behavior at different levels.

**Unit tests** should focus on individual Python/application behaviors.

**Integration tests** exercise Flask routes together with the application logic using Flask's testing capabilities.

**Acceptance tests** verify observable requirements from the perspective of a user or API consumer.

Run the folder:

```bash
python -m pytest python_examples/flask_app -v
```

Run only one testing level:

```bash
python -m pytest python_examples/flask_app -m unit -v
python -m pytest python_examples/flask_app -m integration -v
python -m pytest python_examples/flask_app -m acceptance -v
```

---

### `python_examples/fastapi_app/`

**Purpose:** Demonstrates testing a FastAPI application.

The application files define the API and supporting Python behavior. The test files verify the application at different boundaries.

**Unit tests** test individual functions or logic.

**Integration tests** test API endpoints together with the FastAPI application, typically through a test client.

**Acceptance tests** verify complete externally observable API behavior.

Run:

```bash
python -m pytest python_examples/fastapi_app -v
```

Or:

```bash
python -m pytest python_examples/fastapi_app -m unit -v
python -m pytest python_examples/fastapi_app -m integration -v
python -m pytest python_examples/fastapi_app -m acceptance -v
```

---

### `python_examples/flask_fastapi_shared/`

**Purpose:** Demonstrates testing when Flask and FastAPI expose related or shared application behavior.

This example is particularly useful for discussing **integration testing and contract consistency**.

Students can examine whether the two frameworks:

- use compatible application logic;
- return consistent information;
- preserve the expected API contract.

**Primary test type:** Integration testing.

Run:

```bash
python -m pytest python_examples/flask_fastapi_shared -v
```

---

### `python_examples/streamlit_app/`

**Purpose:** Demonstrates that Streamlit applications can contain both ordinary Python logic and UI behavior.

The example separates two important testing concerns:

**Unit tests** test Python functions without needing to interact with the Streamlit interface.

**Acceptance tests** use Streamlit's `AppTest` functionality to exercise UI behavior.

Typical acceptance-test import:

```python
from streamlit.testing.v1 import AppTest
```

Run:

```bash
python -m pytest python_examples/streamlit_app -v
```

Or:

```bash
python -m pytest python_examples/streamlit_app -m unit -v
python -m pytest python_examples/streamlit_app -m acceptance -v
```

> Streamlit may display a `missing ScriptRunContext` warning when code is executed outside a normal `streamlit run` session. The final Pytest result (`PASSED`, `FAILED`, or `ERROR`) determines whether the test itself succeeded.

---

### `python_examples/streamlit_fastapi/`

**Purpose:** Demonstrates testing a small multi-component application containing:

```text
User
  ↓
Streamlit UI
  ↓
HTTP request
  ↓
FastAPI API
  ↓
JSON response
  ↓
Streamlit displays the result
```

The `api/` folder contains the **FastAPI API/backend portion**.

The `ui/` folder contains the **Streamlit user-interface portion**.

The `tests/` folder contains tests for the stack.

The testing levels should be interpreted as follows:

| Test level | What is being tested |
|---|---|
| **Unit** | A small function or behavior independently |
| **Integration** | Communication between application components, such as API route + application behavior or UI client + API contract |
| **Acceptance** | Observable application/UI behavior from the user's perspective |

Run all tests for this example:

```bash
python -m pytest python_examples/streamlit_fastapi -v
```

Run by testing level:

```bash
python -m pytest python_examples/streamlit_fastapi -m unit -v
python -m pytest python_examples/streamlit_fastapi -m integration -v
python -m pytest python_examples/streamlit_fastapi -m acceptance -v
```

For Streamlit acceptance testing, the tests may use:

```python
from streamlit.testing.v1 import AppTest
```

---

## 4. How to Identify Which Test Is Which

The repository uses Pytest markers to identify testing levels.

A unit test is marked:

```python
@pytest.mark.unit
def test_example():
    ...
```

An integration test is marked:

```python
@pytest.mark.integration
def test_example():
    ...
```

An acceptance test is marked:

```python
@pytest.mark.acceptance
def test_example():
    ...
```

Therefore, students should not determine the testing level only from the filename. They should also inspect the test's **marker and testing boundary**.

A useful rule is:

```text
One isolated behavior
        ↓
      UNIT

Multiple real components
working together
        ↓
   INTEGRATION

User/stakeholder requirement
or observable behavior
        ↓
   ACCEPTANCE
```

---

## 5. TDD Lab

### `tdd_lab/`

**Purpose:** Demonstrates **Test-Driven Development (TDD)**.

TDD follows:

```text
RED
Write a test that fails.
        ↓
GREEN
Write the minimum code needed to pass.
        ↓
REFACTOR
Improve the implementation while
keeping the tests passing.
```

The `starter/` material is intended for students to complete.

Students should begin with the failing test rather than starting with the implementation.

The starter is excluded from the normal repository-wide Pytest execution because a failing test is part of the exercise.

---

## 6. AI-Assisted Testing

### `ai_testing/`

**Purpose:** Demonstrates how AI can assist with test development while emphasizing that generated tests still require human review.

Activities can include:

- generating candidate test cases;
- identifying missing edge cases;
- suggesting assertions;
- reviewing existing tests;
- identifying weak tests;
- critiquing AI-generated tests.

Students should evaluate generated tests rather than automatically accepting them.

Important questions include:

- Does the generated test test the correct requirement?
- Are the assertions meaningful?
- Are edge cases included?
- Is the test actually independent?
- Is the AI testing implementation details instead of behavior?

---

## 7. Node.js, Express, and Istanbul

### `node_istanbul/`

**Purpose:** Provides the JavaScript counterpart to the Python testing examples.

The folder demonstrates:

- Node.js/Express application testing;
- unit testing;
- integration testing;
- acceptance testing;
- JavaScript code coverage.

Install dependencies:

```bash
cd node_istanbul
npm install
```

Run tests:

```bash
npm test
```

Run coverage:

```bash
npm run coverage
```

`nyc` is Istanbul's command-line interface. The coverage command produces terminal coverage information and an HTML report under:

```text
node_istanbul/coverage/
```

If `npm audit` reports a dependency vulnerability, inspect the dependency tree before using `npm audit fix --force`, because `--force` may introduce breaking dependency changes.

---

## 8. Python Environment Setup

From the repository root:

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Using `python -m pytest` is recommended in this repository because it ensures that Pytest runs with the same Python interpreter as the active environment.

---

## 9. Running the Python Tests

### Run all normal tests

```bash
python -m pytest
```

### Show individual test names

```bash
python -m pytest -v
```

### Run unit tests only

```bash
python -m pytest -m unit -v
```

### Run integration tests only

```bash
python -m pytest -m integration -v
```

### Run acceptance tests only

```bash
python -m pytest -m acceptance -v
```

### Show `print()` output during tests

```bash
python -m pytest -m unit -v -s
```

The same option works for the other testing levels:

```bash
python -m pytest -m integration -v -s
python -m pytest -m acceptance -v -s
```

---

## 10. Python Code Coverage

Python coverage requires the `pytest-cov` plugin.

Install it if necessary:

```bash
python -m pip install pytest-cov
```

Run coverage for the Python examples:

```bash
python -m pytest --cov=python_examples --cov-report=term-missing
```

The report includes:

| Column | Meaning |
|---|---|
| `Stmts` | Number of executable statements |
| `Miss` | Statements that were not executed |
| `Cover` | Percentage of statements executed |
| `Missing` | Line numbers not executed by the tests |

Coverage can also be compared by testing level:

```bash
python -m pytest -m unit --cov=python_examples --cov-report=term-missing
python -m pytest -m integration --cov=python_examples --cov-report=term-missing
python -m pytest -m acceptance --cov=python_examples --cov-report=term-missing
```

Remember:

> **Coverage measures execution, not correctness.**

A test suite can achieve high coverage and still contain weak assertions or miss important requirements.

---

## 11. Continuous Integration

### `.github/workflows/tests.yml`

This file defines the repository's automated testing workflow.

It demonstrates how tests can become part of a development pipeline rather than something that developers run only manually.

A typical CI flow is:

```text
Developer pushes code
        ↓
GitHub Actions starts
        ↓
Dependencies are installed
        ↓
Automated tests run
        ↓
Tests pass or fail
        ↓
Result informs review/merge decision
```

Students should inspect this file after learning how to run the same tests locally.

---

## 12. Suggested Teaching Sequence

1. Start with `python_examples/core_unit/` to introduce assertions, edge cases, and parametrization.
2. Move to `python_examples/flask_app/` or `python_examples/fastapi_app/` to show how an API introduces integration boundaries.
3. Compare **unit**, **integration**, and **acceptance** tests in the same application.
4. Use `python_examples/streamlit_app/` to introduce UI acceptance testing with `AppTest`.
5. Use `python_examples/streamlit_fastapi/` to show a multi-component application and explain why integration testing becomes important.
6. Complete the `tdd_lab/` exercise using Red → Green → Refactor.
7. Use `ai_testing/` to discuss AI-assisted test generation and why generated tests still require review.
8. Run Python coverage with `pytest-cov`.
9. Move to `node_istanbul/` to compare Python coverage with JavaScript/Istanbul coverage.
10. Inspect `.github/workflows/tests.yml` to show how the tests become part of CI.

---

## 13. Quick Command Reference

| Goal | Command |
|---|---|
| Run all Python tests | `python -m pytest` |
| Show test names | `python -m pytest -v` |
| Unit tests | `python -m pytest -m unit -v` |
| Integration tests | `python -m pytest -m integration -v` |
| Acceptance tests | `python -m pytest -m acceptance -v` |
| Unit tests + printed output | `python -m pytest -m unit -v -s` |
| Integration + printed output | `python -m pytest -m integration -v -s` |
| Acceptance + printed output | `python -m pytest -m acceptance -v -s` |
| Python coverage | `python -m pytest --cov=python_examples --cov-report=term-missing` |
| Node tests | `cd node_istanbul && npm test` |
| Istanbul coverage | `cd node_istanbul && npm run coverage` |

---

## Instructor Notes

The examples are intentionally small so that students can clearly identify the boundary between testing levels. They are **teaching examples, not production architectures**.

When discussing a test, ask students to identify:

1. **What behavior is being tested?**
2. **What components participate in the test?**
3. **What is mocked or isolated?**
4. **What is the expected result?**
5. **Why is this a unit, integration, or acceptance test?**

Those questions are often more useful than simply memorizing the names of the testing levels.
