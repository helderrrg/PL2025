import ply.lex as lex
import json
import sys

try:
    with open('stock.json', 'r') as f:
        stock = json.load(f)
except FileNotFoundError:
    stock = []

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'CODIGO',
    'VALOR',
    'VIRGULA',
    'PONTO'
]

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_MOEDA(t):
    r'MOEDA'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    return t

def t_SAIR(t):
    r'SAIR'
    return t

def t_CODIGO(t):
    r'[A-Z]\d\d'
    return t

def t_VALOR(t):
    r'\d+[ce]?'
    return t

t_VIRGULA = r','  
t_PONTO = r'\.'  

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"[LEXER] Caráter não reconhecido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

balance = 0.0
inserted_coins = []

def process_command(user_input):
    global balance
    global inserted_coins

    lexer.input(user_input)

    cmd = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        cmd.append(tok)
    
    if not cmd:
        return
    
    if cmd[0].type == 'LISTAR':
        print("cod | nome | quantidade | preço")
        print("---------------------------------")
        for product in stock:
            print(f"{product['cod']} | {product['nome']} | {product['quant']} | {product['preco']:.2f}€")
    elif cmd[0].type == 'MOEDA':
        coins = []
        i = 1
        while i < len(cmd):
            if cmd[i].type == 'VALOR':
                value = cmd[i].value
                if value.endswith('c'):
                    coin = int(value[:-1]) / 100
                elif value.endswith('e'):
                    coin = int(value[:-1])
                else:
                    coin = int(value)
                coins.append(coin)
            i += 1
        balance += sum(coins)
        inserted_coins.extend(coins)
        formatted_balance = f"{balance:.2f}".replace('.', 'e') + 'c'
        print(f"maq: Saldo = {formatted_balance}")
    elif cmd[0].type == 'SELECIONAR':
        if len(cmd) < 2 or cmd[1].type != 'CODIGO':
            print("maq: Comando inválido. Use SELECIONAR <codigo_produto>")
            return
        code = cmd[1].value
        product = next((p for p in stock if p['cod'] == code), None)        
        if not product:
            print("maq: Produto não existe no stock.")
            return
        if product['quant'] == 0:
            print("maq: Produto esgotado.")
            return
        price = product['preco']
        if balance >= price:
            product['quant'] -= 1
            print(f"maq: Pode retirar o produto dispensado: \"{product['nome']}\"")
            balance -= price
            formatted_balance = f"{balance:.2f}".replace('.', 'e') + 'c'
            print(f"maq: Saldo = {formatted_balance}")
        else:
            print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
            formatted_balance = f"{balance:.2f}".replace('.', 'e') + 'c'
            formatted_price = f"{price:.2f}".replace('.', 'e') + 'c'
            print(f"maq: Saldo = {formatted_balance}; Pedido = {formatted_price}")
    elif cmd[0].type == 'SAIR':
        change = calculate_change(balance)
        print("maq: Pode retirar o troco: ", ", ".join(change))
        inserted_coins = []
        balance = 0.0
        print("maq: Até à próxima!")
        with open('stock.json', 'w') as f:
            json.dump(stock, f)
        sys.exit()
    else:
        print("maq: Comando não reconhecido.")

def calculate_change(value):
    change = []
    available_coins = [0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]
    available_coins.sort(reverse=True)

    for coin in available_coins:
        while value >= coin:
            change.append(coin)
            value -= coin
    
    out = []
    count = {}
    for c in change:
        count[c] = count.get(c, 0) + 1

    for coin, amount in count.items():
        if coin >= 1:
            out.append(f"{amount}x {int(coin)}e")
        else:
            cents = int(coin * 100)
            out.append(f"{amount}x {cents}c")
    
    return out

def main():
    if stock == []:
        print("maq: 2025-03-13, Stock não carregado, Estado atualizado.")
    else:
        print("maq: 2025-03-13, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        try:
            user_input = input(">> ")
            process_command(user_input)
        except EOFError:
            print("\nmaq: Até à próxima!")
            break

if __name__ == "__main__":
    main()