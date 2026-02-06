from logic.parser import parse
from logic.evaluator import extract_variables, evaluate, classify
from logic.truth_table import generate

expr = input("Digite a expressão lógica: ")
parsed = parse(expr)
variables = extract_variables(parsed)

results = []
for values in generate(variables):
    results.append(evaluate(parsed, variables, values))

print("Classificação:", classify(results))
