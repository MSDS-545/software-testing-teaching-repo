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
```

Run all normal Python tests:

```bash
pytest
```

Run by testing level:

```bash
python -m pytest -m unit
python -m pytest -m integration
python -m pytest -m acceptance
```

Run with coverage:

```bash
pytest --cov=python_examples --cov-report=term-missing
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

## Instructor notes

The examples are intentionally small so students can identify the boundary between testing levels. They are not intended as production architectures. The TDD starter is excluded from the default `pytest` run because it is supposed to fail before implementation.
