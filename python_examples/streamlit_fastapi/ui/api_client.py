import requests


def fetch_status(base_url: str, name: str, score: int) -> dict:
    response = requests.get(
        f"{base_url.rstrip('/')}/api/status",
        params={"name": name, "score": score},
        timeout=2,
    )
    response.raise_for_status()
    return response.json()
