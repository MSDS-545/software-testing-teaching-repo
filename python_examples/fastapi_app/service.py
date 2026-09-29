def classify_score(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "satisfactory"
    return "needs-improvement"
