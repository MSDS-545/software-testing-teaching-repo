from fastapi import FastAPI, HTTPException
from python_examples.flask_fastapi_shared.domain import GreetingService

service = GreetingService()
app = FastAPI()


@app.get("/api/greeting")
def greeting(name: str = ""):
    try:
        return service.build(name)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
