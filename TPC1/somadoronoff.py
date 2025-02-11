import sys

def extrair_numeros(palavra):
    numeros = []
    numero_atual = ""
    
    for caractere in palavra:
        if caractere.isdigit():
            numero_atual += caractere
        else:
            if numero_atual:
                numeros.append(int(numero_atual))
                numero_atual = ""
    
    if numero_atual:
        numeros.append(int(numero_atual))
    
    return numeros

def contem_substring(palavra, chave):
    return chave in palavra.lower()

def somador_on_off():
    soma = 0
    ligado = True
    
    for linha in sys.stdin:
        palavras = linha.split()
        for palavra in palavras:
            if contem_substring(palavra, "on"):
                ligado = True
            elif contem_substring(palavra, "off"):
                ligado = False
            elif contem_substring(palavra, "="):
                print(soma)
            else:
                numeros = extrair_numeros(palavra)
                if ligado:
                    soma += sum(numeros)

somador_on_off()
