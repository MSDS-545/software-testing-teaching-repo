from fastapi import FastAPI, HTTPException

app = FastAPI(title="Student Status API")


def student_status(name: str, score: int) -> dict:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name is required")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return {
        "name": cleaned,
        "score": score,
        "status": "on-track" if score >= 70 else "needs-support",
    }


@app.get("/api/status")
def status(name: str, score: int):
    try:
        return student_status(name, score)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
