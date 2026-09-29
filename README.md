# Software Testing Teaching Repository

A classroom repository for teaching **unit testing, integration testing, acceptance testing, test-driven development (TDD), AI-assisted testing, and Istanbul code coverage** across Python and JavaScript web stacks.

## Learning map

| Folder | Stack | Primary testing concepts |
|---|---|---|
| `python_examples/core_unit` | Python | Unit tests, edge cases, parametrization |
| `python_examples/flask_app` | Flask | Unit, API integration, acceptance tests |
| `python_examples/fastapi_app` | FastAPI | Unit, API integration, acceptance tests |
| `python_examples/flask_fastapi_shared` | Flask + FastAPI | Shared-domain testing and contract consistency |
| `python_examples/streamlit_app` | Streamlit | Pure-function unit tests + UI acceptance tests with `AppTest` |
| `python_examples/streamlit_fastapi` | Streamlit + FastAPI | Backend integration, mocked client tests, UI acceptance |
| `tdd_lab` | Python | Red → Green → Refactor exercise |
| `ai_testing` | Python | AI-assisted test generation and test-quality critique |
| `node_istanbul` | Node.js + Express | Unit/integration/acceptance tests + Istanbul coverage |

## 1. Python setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate       # Windows PowerShell
pip install -r requirements.txt



******
source .venv/bin/activate

python -c "import streamlit; print(streamlit.__version__)"
python -c "from streamlit.testing.v1 import AppTest; print('AppTest works')"

python -m pytest

python -m pip show streamlit

which python
```

Run all normal Python tests:

```bash
pytest
```

Run by testing level:

```bash
python -m pytest -m unit
python -m pytest -m unit -v
python -m pytest -m unit -v -s
python -m pytest -m unit -v -s
python -m pytest -m integration
python -m pytest -m integration -v
python -m pytest -m integration -v -s
python -m pytest -m acceptance
python -m pytest -m acceptance -v
python -m pytest -m acceptance -v -s


*************
# Unit OR integration
python -m pytest -m "unit or integration" -v

# Integration OR acceptance
python -m pytest -m "integration or acceptance" -v

# Everything except unit tests
python -m pytest -m "not unit" -v

# All tests
python -m pytest -v



**************
UNIT
"Does this function work?"
       ↓
python -m pytest -m unit -v

INTEGRATION
"Do these components work together?"
       ↓
python -m pytest -m integration -v

ACCEPTANCE
"Does the application satisfy the user behavior?"
       ↓
python -m pytest -m acceptance -v


@pytest.mark.integration
def test_api_integration():
    ...


@pytest.mark.acceptance
def test_user_can_get_greeting():
    ...

Does create_greeting("Student") return the correct string?


Does the FastAPI endpoint call the greeting logic and return the expected JSON?


Can a user enter a name in Streamlit, click the button, and see the expected result?



Streamlit then creates a ScriptRunContext for things such as:
st.title()
st.button()
st.text_input()
st.session_state
```
pip install pytest-cov
Run with coverage:

```bash
python -m pip install pytest-cov
python -m pytest --cov=python_examples --cov-report=term-missing
```

## 2. Node.js / Istanbul setup

```bash
cd node_istanbul
npm install
npm test
npm run coverage
```

`nyc` is Istanbul's command-line interface. The coverage command creates a terminal report and an HTML report under `node_istanbul/coverage/`.

## Suggested teaching sequence

1. **Unit testing:** begin with `python_examples/core_unit`.
2. **Integration testing:** move to Flask and FastAPI test clients.
3. **Acceptance testing:** use the Given/When/Then tests in the web examples and Streamlit `AppTest`.
4. **TDD:** complete `tdd_lab/starter` without looking at the solution.
5. **AI-assisted testing:** use the prompt activities in `ai_testing/README.md`, then critique generated tests rather than accepting them automatically.
6. **Coverage:** run Python coverage and then Istanbul coverage in `node_istanbul`.
7. **CI:** inspect `.github/workflows/tests.yml` to see how tests become an automated merge/deployment defense.

## Testing vocabulary used in this repository

- **Unit test:** isolates a small behavior, function, or class.
- **Integration test:** verifies that two or more real components work together, such as a route plus service layer.
- **Acceptance test:** checks observable behavior from a user/stakeholder perspective, often expressed as Given/When/Then.
- **TDD:** write a failing test first (**Red**), implement the smallest behavior that passes (**Green**), then improve the design while tests remain green (**Refactor**).
- **Coverage:** measures which code was executed by a test suite; high coverage does not itself prove correctness.


