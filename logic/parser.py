def parse(expression: str) -> str:
    replacements = {
        "¬": "not ",
        "∧": " and ",
        "∨": " or ",
        "→": " <= ",
        "↔": " == "
    }

    for symbol, value in replacements.items():
        expression = expression.replace(symbol, value)

    return expression
