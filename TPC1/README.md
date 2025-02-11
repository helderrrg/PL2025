# PL 2024/25 - TPC 1

## Problema proposto

Procura-se um programa Python que:

 1. Some todas as sequências de dígitos num texto;
 2. Sempre que encontrar a string `Off`, em qualquer combinação de maiúsculas e minúsculas, o
    comportamento de soma é desligado;
 3. Sempre que encontrar a string `On`, em qualquer combinação de maiúsculas e minúsculas, o
    comportamento de soma é ligado;
 4. Sempre que encontrar o caráter `=`, o resultado da soma é colocado na saída.

Não é permitido o uso de expressões regulares.

## Exemplos

Perante a seguinte fonte:

<pre>
12@~00of<b>on</b>01ff<b>off</b>01<b>on=off</b>??15<b>on</b>1<b>=</b>
</pre>

A saída do programa deve ser:

```
13
14
```

## Explicação da solução

O programa `somador_on_off` lê um ficheiro de texto e percorre o seu conteúdo palavra por palavra. A sua lógica baseia-se num estado de ativação booleano (on/off) que controla se os dígitos encontrados devem ser somados ou ignorados.

## Execução

O programa é executado pelo terminal, passando o ficheiro de *input* como argumento. 

```
$ python main.py <input_file>
```

## Autor  

- **Nome:** Hélder Ricardo Ribeiro Gomes 
- **Número de aluno:** A104100