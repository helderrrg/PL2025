import ply.yacc as yacc
import sys
from exp_lex import tokens

def p_global(p):
    """
    S : ExpAS
    """
    print("Expression value: ", p[1])

def p_expAS_add(p):
    """
    ExpAS : ExpAS ADD ExpMD
    """
    p[0] = p[1] + p[3]

def p_expAS_sub(p):
    """
    ExpAS : ExpAS SUB ExpMD
    """
    p[0] = p[1] - p[3]

def p_expAS_expMD(p):
    """
    ExpAS   : ExpMD
    """
    p[0] = p[1]

def p_expMD_mul(p):
    """
    ExpMD : ExpMD MUL Termo
    """
    p[0] = p[1] * p[3]

def p_expMD_div(p):
    """
    ExpMD : ExpMD DIV Termo
    """
    p[0] = p[1] / p[3]

def p_expMD_termo(p):
    """
    ExpMD   : Termo
    """
    p[0] = p[1]

def p_termo(p):
    """
    Termo : NUM
    """
    p[0] = p[1]

def p_error(p):
    print("Erro sintático",p)
    parser.success = False

parser = yacc.yacc()

for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print("Valid: ", line)
    else:
        print("Invalid sentence.")