# TDD Lab — Password Policy

Goal: implement `is_valid_password()` using **Red → Green → Refactor**.

Start here:

```bash
pytest tdd_lab/starter/test_password_policy_tdd.py -q
```

The starter intentionally fails.

Requirements to discover one test at a time:

1. Password must contain at least 8 characters.
2. Password must contain at least one digit.
3. Password must contain at least one uppercase letter.

Do not implement all requirements at once. Add one failing test, make it pass with the smallest change, then refactor.
