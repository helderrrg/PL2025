# PL 2024/25 - TPC5

## 📖 Resumo
O objetivo deste programa é um **analisador sintático recursivo descendente** de expressões matemáticas simples, garantindo que a ordem das operações está corretamente implementada.
O programa interpreta e avalia expressões aritméticas que envolvem números inteiros e as operações **adição (+)**, **subtração (-)**, **multiplicação (*)** e **divisão (/)**, respeitando a prioridade dos operadores.

## Conteúdo

#### Tokens:
- `NUM`: Representa os números inteiros;
- `ADD`: Representa o operador `+`;
- `SUB`: Representa o operador `-`;
- `MUL`: Representa o operador `*`;
- `DIV`: Representa o operador `/`.

#### Expressões Regulares:
- `t_ADD = r'\+'`
- `t_SUB = r'\-'`
- `t_MUL = r'\*'`
- `t_DIV = r'\/'`
- `t_NUM = r'\d+'`

#### Gramática:

```
T = {num, '+','-','*','/'}
S = ExpAS
N = {ExpAS, ExpMD, Termo, Num}
P = {
    ExpAS  -> ExpAS ADD ExpMD
          | ExpAS SUB ExpMD
          | ExpMD
    ExpMD  -> ExpMD MUL Termo
          | ExpMD DIV Termo
          | Termo
    Termo -> NUM
}
```

## 📂 Resultados
Segue a localização dos ficheiros produzidos:
- [`exp_lex.py`](exp_lex.py) - [Ficheiro com o léxico]
- [`exp_sin.json`](exp_sin.json) - [Ficheiro com a sintax]

## Autor  

- **Nome:** Hélder Ricardo Ribeiro Gomes 
- **Número de aluno:** A104100
---