# Software Testing Teaching Repository

A classroom repository for teaching **unit testing, integration testing,
acceptance testing, test-driven development (TDD), AI-assisted testing,
and code coverage** across Python and JavaScript web stacks.

The examples are intentionally small. The goal is to help students see
**what is being tested, which components participate in the test, and
why a test is classified as unit, integration, or acceptance testing**.

------------------------------------------------------------------------

## 1. Repository Learning Map

  --------------------------------------------------------------------------------------------------
  Folder                                    Technology        What the folder      Test levels
                                                              demonstrates         
  ----------------------------------------- ----------------- -------------------- -----------------
  `python_examples/core_unit/`              Python            Small Python         **Unit**
                                                              functions tested     
                                                              independently        

  `python_examples/flask_app/`              Flask             Flask application    **Unit,
                                                              behavior, API        Integration,
                                                              interactions, and    Acceptance**
                                                              user-facing          
                                                              requirements         

  `python_examples/fastapi_app/`            FastAPI           FastAPI application  **Unit,
                                                              logic and API        Integration,
                                                              endpoint behavior    Acceptance**

  `python_examples/flask_fastapi_shared/`   Flask + FastAPI   Multiple frameworks  **Integration /
                                                              using shared         Contract
                                                              domain/application   consistency**
                                                              behavior             

  `python_examples/streamlit_app/`          Streamlit         Testable Python      **Unit,
                                                              logic plus Streamlit Acceptance**
                                                              UI behavior          

  `python_examples/streamlit_fastapi/`      Streamlit +       Streamlit UI         **Unit,
                                            FastAPI           communicating with a Integration,
                                                              FastAPI service      Acceptance**

  `tdd_lab/`                                Python            Red → Green →        **TDD / Unit**
                                                              Refactor workflow    

  `ai_testing/`                             Python +          Generating,          **Test design
                                            AI-assisted       reviewing, and       activity**
                                            workflow          improving tests with 
                                                              AI assistance        

  `node_istanbul/`                          Node.js + Express JavaScript testing   **Unit,
                                                              and Istanbul/NYC     Integration,
                                                              coverage             Acceptance**

  `.github/workflows/`                      GitHub Actions    Automatic execution  **Continuous
                                                              of tests in CI       Integration**
  --------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 2. Understanding the Test Levels

### Unit Testing

A **unit test** checks one small piece of application behavior in
isolation.

Examples include:

-   testing one Python function;
-   testing validation logic;
-   testing a calculation;
-   testing an individual JavaScript function;
-   testing edge cases with parametrized input.

The main question is:

> **Does this individual unit of code work correctly?**

Run only tests marked `unit`:

``` bash
python -m pytest -m unit -v
```

------------------------------------------------------------------------

### Integration Testing

An **integration test** verifies that multiple application components
work together correctly.

Examples include:

-   a FastAPI route working with application logic;
-   a Flask route returning the expected API response;
-   a Streamlit client correctly communicating with FastAPI;
-   multiple services agreeing on a shared response contract.

The main question is:

> **Do these components work correctly when connected?**

Run only tests marked `integration`:

``` bash
python -m pytest -m integration -v
```

------------------------------------------------------------------------

### Acceptance Testing

An **acceptance test** checks whether the application satisfies an
observable user or stakeholder requirement.

Examples include:

-   a user enters a name and receives the expected greeting;
-   a Streamlit interface displays the expected result;
-   an HTTP request produces the behavior required by the application
    specification.

Acceptance tests may be written using **Given / When / Then**:

``` text
Given the application is available
When the user performs an action
Then the expected behavior should occur
```

The main question is:

> **Does the application behave the way the user expects?**

Run only tests marked `acceptance`:

``` bash
python -m pytest -m acceptance -v
```

------------------------------------------------------------------------

## 3. Python Examples

### `python_examples/core_unit/`

**Purpose:** Introduces unit testing without the additional complexity
of a web framework.

Students should use this folder first.

The application/source files contain small Python behaviors. The test
files exercise those behaviors independently.

**Primary test type:** Unit testing.

Concepts demonstrated include:

-   assertions;
-   expected versus actual results;
-   normal cases;
-   edge cases;
-   parametrized tests.

Run:

``` bash
python -m pytest python_examples/core_unit -v
```

Or run all tests marked as unit tests:

``` bash
python -m pytest -m unit -v
```

------------------------------------------------------------------------

### `python_examples/flask_app/`

**Purpose:** Demonstrates how testing changes when application behavior
is exposed through Flask routes.

The folder contains the Flask application code and tests that examine
behavior at different levels.

**Unit tests** should focus on individual Python/application behaviors.

**Integration tests** exercise Flask routes together with the
application logic using Flask's testing capabilities.

**Acceptance tests** verify observable requirements from the perspective
of a user or API consumer.

Run the folder:

``` bash
python -m pytest python_examples/flask_app -v
```

Run only one testing level:

``` bash
python -m pytest python_examples/flask_app -m unit -v
python -m pytest python_examples/flask_app -m integration -v
python -m pytest python_examples/flask_app -m acceptance -v
```

------------------------------------------------------------------------

### `python_examples/fastapi_app/`

**Purpose:** Demonstrates testing a FastAPI application.

The application files define the API and supporting Python behavior. The
test files verify the application at different boundaries.

**Unit tests** test individual functions or logic.

**Integration tests** test API endpoints together with the FastAPI
application, typically through a test client.

**Acceptance tests** verify complete externally observable API behavior.

Run:

``` bash
python -m pytest python_examples/fastapi_app -v
```

Or:

``` bash
python -m pytest python_examples/fastapi_app -m unit -v
python -m pytest python_examples/fastapi_app -m integration -v
python -m pytest python_examples/fastapi_app -m acceptance -v
```

------------------------------------------------------------------------

### `python_examples/flask_fastapi_shared/`

**Purpose:** Demonstrates testing when Flask and FastAPI expose related
or shared application behavior.

This example is particularly useful for discussing **integration testing
and contract consistency**.

Students can examine whether the two frameworks:

-   use compatible application logic;
-   return consistent information;
-   preserve the expected API contract.

**Primary test type:** Integration testing.

Run:

``` bash
python -m pytest python_examples/flask_fastapi_shared -v
```

------------------------------------------------------------------------

### `python_examples/streamlit_app/`

**Purpose:** Demonstrates that Streamlit applications can contain both
ordinary Python logic and UI behavior.

The example separates two important testing concerns:

**Unit tests** test Python functions without needing to interact with
the Streamlit interface.

**Acceptance tests** use Streamlit's `AppTest` functionality to exercise
UI behavior.

Typical acceptance-test import:

``` python
from streamlit.testing.v1 import AppTest
```

Run:

``` bash
python -m pytest python_examples/streamlit_app -v
```

Or:

``` bash
python -m pytest python_examples/streamlit_app -m unit -v
python -m pytest python_examples/streamlit_app -m acceptance -v
```

> Streamlit may display a `missing ScriptRunContext` warning when code
> is executed outside a normal `streamlit run` session. The final Pytest
> result (`PASSED`, `FAILED`, or `ERROR`) determines whether the test
> itself succeeded.

------------------------------------------------------------------------

### `python_examples/streamlit_fastapi/`

**Purpose:** Demonstrates testing a small multi-component application
containing:

``` text
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

The current example is organized as:

``` text
python_examples/streamlit_fastapi/
├── api/
│   ├── __init__.py
│   └── api.py
├── ui/
│   ├── __init__.py
│   ├── api_client.py
│   └── ui.py
└── tests/
    ├── __init__.py
    └── test_stack.py
```

-   `api/api.py` contains the **FastAPI backend** and status logic.
-   `ui/ui.py` contains the **Streamlit user interface**.
-   `ui/api_client.py` contains the HTTP client used by Streamlit to
    call FastAPI.
-   `tests/test_stack.py` contains the **unit, integration, and
    acceptance tests**.

For Streamlit `AppTest`, locate the UI relative to the test file so the
same test works locally and in GitHub Actions:

``` python
from pathlib import Path

ui_file = Path(__file__).resolve().parent.parent / "ui" / "ui.py"
at = AppTest.from_file(str(ui_file))
```

The testing levels should be interpreted as follows:

  -----------------------------------------------------------------------
  Test level                          What is being tested
  ----------------------------------- -----------------------------------
  **Unit**                            A small function or behavior
                                      independently

  **Integration**                     Communication between application
                                      components, such as API route +
                                      application behavior or UI client +
                                      API contract

  **Acceptance**                      Observable application/UI behavior
                                      from the user's perspective
  -----------------------------------------------------------------------

Run all tests for this example:

``` bash
python -m pytest python_examples/streamlit_fastapi -v
```

Run by testing level:

``` bash
python -m pytest python_examples/streamlit_fastapi -m unit -v
python -m pytest python_examples/streamlit_fastapi -m integration -v
python -m pytest python_examples/streamlit_fastapi -m acceptance -v
```

For Streamlit acceptance testing, the tests may use:

``` python
from streamlit.testing.v1 import AppTest
```

------------------------------------------------------------------------

## 4. How to Identify Which Test Is Which

The repository uses Pytest markers to identify testing levels.

A unit test is marked:

``` python
@pytest.mark.unit
def test_example():
    ...
```

An integration test is marked:

``` python
@pytest.mark.integration
def test_example():
    ...
```

An acceptance test is marked:

``` python
@pytest.mark.acceptance
def test_example():
    ...
```

Therefore, students should not determine the testing level only from the
filename. They should also inspect the test's **marker and testing
boundary**.

A useful rule is:

``` text
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

------------------------------------------------------------------------

## 5. TDD Lab

### `tdd_lab/`

**Purpose:** Demonstrates **Test-Driven Development (TDD)**.

TDD follows:

``` text
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

Students should begin with the failing test rather than starting with
the implementation.

The starter is excluded from the normal repository-wide Pytest execution
because a failing test is part of the exercise.

------------------------------------------------------------------------


## 7. Node.js, Express, and Istanbul

### `node_istanbul/`

**Purpose:** Provides the JavaScript counterpart to the Python testing
examples.

The folder demonstrates:

-   Node.js/Express application testing;
-   unit testing;
-   integration testing;
-   acceptance testing;
-   JavaScript code coverage.

Install dependencies:

``` bash
cd node_istanbul
npm install
```

Run tests:

``` bash
npm test
```

Run coverage:

``` bash
npm run coverage
```

`nyc` is Istanbul's command-line interface. The coverage command
produces terminal coverage information and an HTML report under:

``` text
node_istanbul/coverage/
```

If `npm audit` reports a dependency vulnerability, inspect the
dependency tree before using `npm audit fix --force`, because `--force`
may introduce breaking dependency changes.

------------------------------------------------------------------------

## 8. Python Environment Setup

From the repository root:

### macOS/Linux

``` bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Using `python -m pytest` is recommended in this repository because it
ensures that Pytest runs with the same Python interpreter as the active
environment.

------------------------------------------------------------------------

## 9. Running the Python Tests

### Run all normal tests

``` bash
python -m pytest
```

### Show individual test names

``` bash
python -m pytest -v
```

### Run unit tests only

``` bash
python -m pytest -m unit -v
```

### Run integration tests only

``` bash
python -m pytest -m integration -v
```

### Run acceptance tests only

``` bash
python -m pytest -m acceptance -v
```

### Show `print()` output during tests

``` bash
python -m pytest -m unit -v -s
```

The same option works for the other testing levels:

``` bash
python -m pytest -m integration -v -s
python -m pytest -m acceptance -v -s
```

------------------------------------------------------------------------

## 10. Python Code Coverage and Visual Test Reports

Coverage measures which source-code statements and branches are executed
by the tests. It does **not** by itself prove that the application is
correct.

### Required reporting packages

Include these packages in `requirements.txt`:

``` text
pytest
pytest-cov
pytest-html
```

Install them when needed:

``` bash
python -m pip install pytest pytest-cov pytest-html
```

### Terminal coverage

``` bash
python -m pytest --cov=python_examples --cov-report=term-missing
```

  Column      Meaning
  ----------- -----------------------------------
  `Stmts`     Executable statements measured
  `Miss`      Statements not executed
  `Cover`     Percentage of statements executed
  `Missing`   Specific unexecuted line numbers

### Branch coverage

Branch coverage checks whether alternative decision paths are exercised.
For an `if/else`, for example, testing only the `if` result does not
demonstrate that the `else` behavior works.

``` bash
python -m pytest --cov=python_examples --cov-branch --cov-report=term-missing
```

### HTML coverage report

``` bash
python -m pytest \
  --cov=python_examples \
  --cov-branch \
  --cov-report=term-missing \
  --cov-report=html
```

This creates:

``` text
htmlcov/
└── index.html
```

Students can click individual source files in this report to see
executed lines, missed lines, branches, and coverage percentages.

Open on macOS:

``` bash
open htmlcov/index.html
```

Open on Windows:

``` powershell
start htmlcov/index.html
```

### HTML test-results report

The coverage report answers **how much code was exercised**. The Pytest
HTML report answers **which tests passed, failed, or were skipped**.

``` bash
python -m pytest -v \
  --html=reports/test-report.html \
  --self-contained-html
```

This creates:

``` text
reports/
└── test-report.html
```

Open on macOS:

``` bash
open reports/test-report.html
```

Open on Windows:

``` powershell
start reports/test-report.html
```

### Recommended command: generate both reports

``` bash
python -m pytest -v \
  --cov=python_examples \
  --cov-branch \
  --cov-report=term-missing \
  --cov-report=html \
  --html=reports/test-report.html \
  --self-contained-html
```

This produces:

``` text
Pytest
  |
  +-- Terminal results
  |
  +-- reports/test-report.html
  |     Passed / Failed / Skipped tests
  |
  +-- htmlcov/index.html
        Statement coverage
        Branch coverage
        Missing lines
        Coverage percentages
```

### Which report should students review?

  ----------------------------------------------------------------------------
  Report                  Location                     What it answers
  ----------------------- ---------------------------- -----------------------
  Pytest terminal output  Terminal                     Did the test run
                                                       succeed?

  Pytest HTML report      `reports/test-report.html`   Which individual tests
                                                       passed or failed?

  Coverage terminal       Terminal                     How many
  report                                               statements/branches
                                                       were exercised?

  Coverage HTML report    `htmlcov/index.html`         Exactly which source
                                                       lines and branches were
                                                       or were not exercised?

  Istanbul report         `node_istanbul/coverage/`    What JavaScript code
                                                       was exercised?
  ----------------------------------------------------------------------------

Students should review **both** Python HTML reports. A suite can have
all tests passing while still leaving important code paths untested.

### Compare coverage by testing level

``` bash
python -m pytest -m unit --cov=python_examples --cov-branch --cov-report=term-missing
python -m pytest -m integration --cov=python_examples --cov-branch --cov-report=term-missing
python -m pytest -m acceptance --cov=python_examples --cov-branch --cov-report=term-missing
```

This comparison helps show how unit, integration, and acceptance tests
exercise different parts of an application.

> **Coverage measures execution, not correctness.** High coverage can
> still accompany weak assertions or missing requirements.

------------------------------------------------------------------------

## 11. Continuous Integration

### `.github/workflows/tests.yml`

This file defines the repository's automated testing workflow.

It demonstrates how tests can become part of a development pipeline
rather than something that developers run only manually.

A typical CI flow is:

``` text
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

Students should inspect this file after learning how to run the same
tests locally.

GitHub Actions can also generate these HTML reports. If
`.github/workflows/tests.yml` is configured to upload them as artifacts,
they can be retrieved from **GitHub → Actions → workflow run →
Artifacts**. The workflow must explicitly upload the generated files;
generating HTML alone does not make it a downloadable Actions artifact.

------------------------------------------------------------------------

## 12. Suggested Teaching Sequence

1.  Start with `python_examples/core_unit/` to introduce assertions,
    edge cases, and parametrization.
2.  Move to `python_examples/flask_app/` or
    `python_examples/fastapi_app/` to show how an API introduces
    integration boundaries.
3.  Compare **unit**, **integration**, and **acceptance** tests in the
    same application.
4.  Use `python_examples/streamlit_app/` to introduce UI acceptance
    testing with `AppTest`.
5.  Use `python_examples/streamlit_fastapi/` to show a multi-component
    application and explain why integration testing becomes important.
6.  Complete the `tdd_lab/` exercise using Red → Green → Refactor.
7.  Use `ai_testing/` to discuss AI-assisted test generation and why
    generated tests still require review.
8.  Run statement and branch coverage with `pytest-cov`.
9.  Open `reports/test-report.html` to review test outcomes visually.
10. Open `htmlcov/index.html` to inspect covered and uncovered lines and
    branches.
11. Move to `node_istanbul/` to compare Python coverage with
    JavaScript/Istanbul coverage.
12. Inspect `.github/workflows/tests.yml` to show how tests and reports
    become part of CI.

------------------------------------------------------------------------

## 13. Quick Command Reference

  ---------------------------------------------------------------------------------------------------------------------
  Goal                                Command
  ----------------------------------- ---------------------------------------------------------------------------------
  Run all Python tests                `python -m pytest`

  Show test names                     `python -m pytest -v`

  Unit tests                          `python -m pytest -m unit -v`

  Integration tests                   `python -m pytest -m integration -v`

  Acceptance tests                    `python -m pytest -m acceptance -v`

  Unit tests + printed output         `python -m pytest -m unit -v -s`

  Integration tests + printed output  `python -m pytest -m integration -v -s`

  Acceptance tests + printed output   `python -m pytest -m acceptance -v -s`

  Statement coverage                  `python -m pytest --cov=python_examples --cov-report=term-missing`

  Branch coverage                     `python -m pytest --cov=python_examples --cov-branch --cov-report=term-missing`

  HTML coverage                       `python -m pytest --cov=python_examples --cov-branch --cov-report=html`

  HTML test report                    `python -m pytest -v --html=reports/test-report.html --self-contained-html`

  Open test HTML on macOS             `open reports/test-report.html`

  Open coverage HTML on macOS         `open htmlcov/index.html`

  Node tests                          `cd node_istanbul && npm test`

  Istanbul coverage                   `cd node_istanbul && npm run coverage`
  ---------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Instructor Notes

The examples are intentionally small so that students can clearly
identify the boundary between testing levels. They are **teaching
examples, not production architectures**.

When discussing a test, identify:

1.  **What behavior is being tested?**
2.  **What components participate in the test?**
3.  **What is mocked or isolated?**
4.  **What is the expected result?**
5.  **Why is this a unit, integration, or acceptance test?**

Those questions are often more useful than simply memorizing the names
of the testing levels.


