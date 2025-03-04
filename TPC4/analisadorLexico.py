import re

token_specs = [
    ("SELECT", r'select'),
    ("WHERE", r'where'),
    ("LIMIT", r'LIMIT'),
    ("VAR", r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
    ("TYPE", r'[a-zA-Z_]*:[a-zA-Z_][a-zA-Z0-9_]*'),
    ("STRING", r'".*?"(@[a-zA-Z]+)?'),
    ("SHORT_TYPE", r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ("DOT", r'\.'),
    ("BRACE_OPEN", r'\{'),
    ("BRACE_CLOSE", r'\}'),
    ("NUMBER", r'\d+'),
    ("WHITESPACE", r'\s+'),
    ("UNKNOWN", r'.')
]

token_re = re.compile('|'.join(f'(?P<{name}>{regex})' for name, regex in token_specs), re.IGNORECASE)

def lexer(query):
    tokens = []
    for match in token_re.finditer(query):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == "WHITESPACE":
            continue
        tokens.append((kind, value))
    return tokens

query = '''
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
'''

tokens = lexer(query)
for token in tokens:
    print(token)
