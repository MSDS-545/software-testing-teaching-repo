class GreetingService:
    def build(self, name: str) -> dict:
        cleaned = name.strip()
        if not cleaned:
            raise ValueError("name is required")
        return {"message": f"Hello, {cleaned}!", "length": len(cleaned)}
