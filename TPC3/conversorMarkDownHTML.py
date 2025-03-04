import sys
import re

def tokenize(code):
    token_specification = [
        ('HEADER', r'^(#{1,3})\s+(.+)'),  # Cabeçalhos (#, ##, ###)
        ('BOLD', r'\*\*(.*?)\*\*'),  # Texto em negrito
        ('ITALIC', r'\*(.*?)\*'),  # Texto em itálico
        ('NUM_LIST', r'^(\d+)\.\s+(.+)'),  # Listas numeradas
        ('LINK', r'\[(.*?)\]\((.*?)\)'),  # Links [texto](URL)
        ('IMAGE', r'!\[(.*?)\]\((.*?)\)'),  # Imagens ![alt](URL)
        ('NEWLINE', r'\n+'),  # Quebra de linha
        ('TEXT', r'[^*\n\[\]!]+'),  # Texto comum
        ('SKIP', r'[ \t]+'),  # Espaços e tabulações
        ('ERROR', r'.'),  # Qualquer outro caractere
    ]
    
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
    tokens = []
    
    for match in re.finditer(tok_regex, code, re.MULTILINE):
        kind = match.lastgroup
        value = match.group()
        
        if kind == 'SKIP':
            continue
        
        tokens.append((kind, value))
    
    return tokens

def markdown_to_html(md_text):
    tokens = tokenize(md_text)
    html_output = []
    
    in_list = False
    
    for i, (kind, value) in enumerate(tokens):
        if kind == 'HEADER':
            if in_list:
                html_output.append('</ol>')
                in_list = False
            level = len(re.match(r'^(#{1,3})', value).group(1))
            text = re.sub(r'^#{1,3}\s+', '', value)
            html_output.append(f'<h{level}>{text}</h{level}>')

        elif kind == 'NUM_LIST':
            if not in_list:
                html_output.append('<ol>')
                in_list = True
            text = re.sub(r'^\d+\.\s+', '', value)
            html_output.append(f'<li>{text}</li>')

        elif kind == 'NEWLINE':
            if in_list and (i + 1 >= len(tokens) or tokens[i + 1][0] != 'NUM_LIST'):
                html_output.append('</ol>')
                in_list = False

        else:
            if in_list:
                html_output.append('</ol>')
                in_list = False

            if kind == 'BOLD':
                html_output.append(f'<b>{value[2:-2]}</b>')
            elif kind == 'ITALIC':
                html_output.append(f'<i>{value[1:-1]}</i>')
            elif kind == 'LINK':
                match = re.match(r'\[(.*?)\]\((.*?)\)', value)
                html_output.append(f'<a href="{match.group(2)}">{match.group(1)}</a>')
            elif kind == 'IMAGE':
                match = re.match(r'!\[(.*?)\]\((.*?)\)', value)
                html_output.append(f'<img src="{match.group(2)}" alt="{match.group(1)}"/>')
            elif kind == 'TEXT':
                html_output.append(f'<p>{value}</p>')

    if in_list:
        html_output.append('</ol>')  # Fecha qualquer lista ainda aberta no final

    return '\n'.join(html_output)

if __name__ == "__main__":
    md_text = sys.stdin.read()
    html_result = markdown_to_html(md_text)
    print(html_result)
