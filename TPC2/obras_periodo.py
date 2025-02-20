import sys
import re

periods = {}

periodo_match = r'\d\d\d\d;(.*?);.*?;'

for line in sys.stdin:
    if "nome;desc" in line:
        continue
    
    match = re.search(periodo_match, line)
    if match:
        periods[match.group(1)] = periods.get(match.group(1), 0) + 1

print("Distribuição das obras por período:")
for key, value in periods.items():
    print(f"{key}: {value}")