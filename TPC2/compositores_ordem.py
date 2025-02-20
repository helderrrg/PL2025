import sys
import re

composers = []

composer_pattern = r'\d\d\d\d;.*?;(.*?);'

for line in sys.stdin:
    if "nome;desc" in line:
        continue
    
    match = re.search(composer_pattern, line)
    if match:
        composers.append(match.group(1))

composers.sort()

print("Lista ordenada alfabeticamente dos compositores musicais:")
for composer in composers:
    print(composer)