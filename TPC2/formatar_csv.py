import re

def formatarCSV(ficheiroEntrada, ficheiroSaida):
    with open(ficheiroEntrada, 'r', encoding='utf-8') as entrada, open(ficheiroSaida, 'w', encoding='utf-8') as saida:
        conteudo = entrada.read()
        
        normalizado = re.sub(r'\n\s+', ' ', conteudo)
        
        saida.write(normalizado)

formatarCSV('obras.csv', 'obras_normalizado.csv')