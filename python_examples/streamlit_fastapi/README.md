# Streamlit + FastAPI demo

Terminal 1:

```bash
uvicorn python_examples.streamlit_fastapi.api:app --reload
```

Terminal 2:

```bash
streamlit run python_examples/streamlit_fastapi/ui.py
```

The automated suite deliberately tests the backend and UI separately for speed and determinism. A live end-to-end browser/API test can be added later with Playwright if desired.
