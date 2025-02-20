import sys
import re

periods = {}

periods_match = r'^(\w.*?);.*\d{4};(.*?);'

for line in sys.stdin:
    if "nome;desc" in line:
        continue

    m = re.search(periods_match, line)
    if m:
        title = m.group(1)
        period = m.group(2)
        periods[period] = periods.get(period, []) + [title]

for chave, valor in periods.items():
    valor.sort()

print("Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período:")
for chave, valor in periods.items():
    print(f"{chave}: {len(valor)}")
    for title in valor:
        print(f"{title}")