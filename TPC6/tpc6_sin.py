import ply.yacc as yacc
from tpc6_lex import tokens, literals

def p_expr(p):
    'expr : term expr2'
    p[0] = p[1] + p[2]

def p_expr2_add(p):
    'expr2 : "+" term expr2'
    p[0] = p[2] + p[3]

def p_expr2_sub(p):
    'expr2 : "-" term expr2'
    p[0] = -p[2] + p[3]

def p_expr2_empty(p):
    'expr2 : '
    p[0] = 0

def p_term(p):
    'term : factor term2'
    p[0] = p[1] * p[2]

def p_term2_mul(p):
    'term2 : "*" factor term2'
    p[0] = p[2] * p[3]

def p_term2_div(p):
    'term2 : "/" factor term2'
    p[0] = p[2] / p[3]

def p_term2_empty(p):
    'term2 : '
    p[0] = 1

def p_factor_num(p):
    'factor : num'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : "(" expr ")"'
    p[0] = p[2]

def p_error(p):
    print('Erro sintático:', p)
    parser.success = False

parser = yacc.yacc()

import sys

for line in sys.stdin:
    parser.success = True
    result = parser.parse(line)
    if parser.success:
        print(f'Frase válida! Valor: {result}')
    else:
        print('Frase inválida... Corrija e tente novamente!')