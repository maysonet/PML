import ply.lex as lex

# Reserved Words
reserved = {
    'new': 'NEW',
    'add': 'ADDuser'
}

# Tokens
tokens = ["NAME", "DATE", "ID", "uNAME"] + list(reserved.values())

# Simple Regular Expressions
t_ignore = ' \t'
t_NAME = r'[a-zA-Z]+'
t_uNAME = r'@[a-zA-Z]+'
t_ID = r'[\d+]+'
t_DATE = r'\d+/[a-zA-Z]+/\d+'

def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''NEW projectName 1 12/may/1231 12/jun/1231 @Chris'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
