# PL 2024/25 - TPC5

## 📖 Resumo
Para resolver o problema de simular uma máquina de vending com persistência de stock e gestão de transações, utilizei o módulo `ply.lex` em Python. O objetivo era criar um programa capaz de interagir com o utilizador através de comandos específicos, gerir um stock de produtos persistente, processar pagamentos com moedas e dispensar produtos ou devolver troco conforme adequado.

### **Estrutura do Programa**
O programa está organizado da seguinte forma:
1. **Carregamento do Stock:** Ao iniciar, o programa carrega o stock a partir de um ficheiro JSON. Se o ficheiro não existir, inicializa um stock vazio.
2. **Analisador Léxico:** Utiliza `ply.lex` para processar comandos de utilizador, reconhecendo palavras-chave como `LISTAR`, `MOEDA`, `SELECIONAR` e `SAIR`.
3. **Gestão de Estado:** Mantém um registo do saldo atual do utilizador e das moedas inseridas durante a sessão.
4. **Processamento de Comandos:** Implementa lógica para lidar com cada tipo de comando, actualizando o stock e o saldo conforme necessário.
5. **Persistência:** Ao terminar, guarda o stock atualizado no ficheiro JSON para manter o estado entre sessões.

#### **Carregamento e Persistência do Stock**
```python
try:
    with open('stock.json', 'r') as f:
        stock = json.load(f)
except FileNotFoundError:
    stock = []
```
O stock é carregado no início do programa. Se o ficheiro não existir, é inicializado um stock vazio.

#### **Analisador Léxico**
Defini regras para reconhecer diferentes tipos de tokens:
- Comandos (`LISTAR`, `MOEDA`, `SELECIONAR`, `SAIR`)
- Código de produto (`CODIGO`)
- Valores de moeda (`VALOR`)
- Separadores como vírgulas e pontos

#### **Processamento de Comandos**
Implementei uma função `process_command` que analisa a entrada do utilizador e executa a ação correspondente:
- **LISTAR:** Mostra o stock atual com detalhes de cada produto.
- **MOEDA:** Processa as moedas inseridas, actualizando o saldo.
- **SELECIONAR:** Verifica se o produto existe e se há saldo suficiente para dispensá-lo.
- **SAIR:** Calcula e devolve o troco, guardando o stock atualizado.

#### **Cálculo de Troco**
A função `calculate_change` determina as moedas a devolver, utilizando um sistema guloso para dar o menor número de moedas possível.

## 📂 Resultados
Segue a localização dos ficheiros produzidos:
- [`tpc5.py`](tpc5.py) - [Ficheiro com código fonte]
- [`stock.json`](stock.json) - [Ficheiro de persistência do stock]

## Autor  

- **Nome:** Hélder Ricardo Ribeiro Gomes 
- **Número de aluno:** A104100
---