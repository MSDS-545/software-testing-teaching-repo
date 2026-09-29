"""Small pure functions for unit-testing demonstrations."""


def final_price(subtotal: float, member: bool = False) -> float:
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    discount = 0.10 if member and subtotal >= 100 else 0.0
    return round(subtotal * (1 - discount), 2)


def shipping_cost(subtotal: float) -> float:
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if subtotal >= 75:
        return 0.0
    return 7.99
