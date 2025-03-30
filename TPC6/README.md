# 📌 TPC6 - Parser LL(1) para Expressões Aritméticas

## 📅 Data
2025-03-30

## 👤 Autor
- **Nome:** Hélder Ricardo Ribeiro Gomes
- **Número de Aluno:** A104100

## 📖 Resumo
Neste trabalho, implementei um parser LL(1) recursivo descendente usando `ply.lex` e `ply.yacc` para reconhecer expressões aritméticas e calcular seus valores. O objetivo era criar um analisador sintático capaz de processar expressões com adição, subtração, multiplicação, divisão e parênteses, respeitando a precedência e associatividade dos operadores.

### **Estrutura do Programa**
A solução está organizada da seguinte forma:
1. **Lexer:** Utiliza `ply.lex` para tokenizar a entrada, reconhecendo números, operadores e parênteses.
2. **Parser LL(1):** Implementa uma gramática LL(1) com regras para `expr`, `term` e `factor` para garantir a precedência correta dos operadores.
3. **Cálculo de Valores:** Cada regra de produção calcula o valor da subexpressão correspondente, acumulando resultados parciais.
4. **Gestão de Erros:** Deteta e reporta erros sintáticos na entrada.

#### **Lexer**
O lexer reconhece os seguintes tokens:
- Números inteiros (`num`)
- Operadores (`+`, `-`, `*`, `/`)
- Parênteses (`(`, `)`)

#### **Gramática LL(1)**
A gramática implementada é:
```
expr -> term expr2
expr2 -> '+' term expr2
    | '-' term expr2
    | ε
term -> factor term2
term2 -> '*' factor term2
    | '/' factor term2
    | ε
factor -> num
    | '(' expr ')'
```

#### **Cálculo de Expressões**
Cada regra de produção calcula o valor da expressão:
- **`expr`** soma ou subtrai valores de `term`
- **`term`** multiplica ou divide valores de `factor`
- **`factor`** representa valores finais (números ou expressões entre parênteses)

### **Resultados**
Segue a localização dos ficheiros produzidos:
- [`num_lex.py`](num_lex.py) - [Lexer para reconhecimento de tokens]
- [`num_yacc.py`](num_yacc.py) - [Parser LL(1) com cálculo de valores]

#### **Exemplos de Saída**
1. **Entrada:** `2+3`
   - **Saída:** `Frase válida! Valor: 5`

2. **Entrada:** `67-(2+3*4)`
   - **Saída:** `Frase válida! Valor: 53`

3. **Entrada:** `(9-2)*(13-4)`
   - **Saída:** `Frase válida! Valor: 63`

---