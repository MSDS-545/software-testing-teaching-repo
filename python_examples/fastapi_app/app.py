from fastapi import FastAPI, HTTPException
from python_examples.fastapi_app.service import classify_score

app = FastAPI(title="Testing Demo API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/result/{score}")
def result(score: int):
    try:
        label = classify_score(score)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"score": score, "classification": label}
