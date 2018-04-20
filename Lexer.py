import ply.lex as lex

# Reserved Words
reserved = {
    'new': 'NEW',
    'user': 'USER',
    'task': 'TASK'
}

# Tokens
tokens = ["NAME", "DATE", "ID"] + list(reserved.values())

# Simple Regular Expressions
t_ignore = ' \t'
t_NAME = r'[a-zA-Z]+'
t_ID = r'[\d+]+'
## NEED regular expression to accept characters and spaces - for tasks

#date format: 2012-02-20 -- year-month-day
t_DATE = r'\d+-\d+-\d+'

def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''NEW projectName 1 2012-02-20 2012-02-26 @Chris'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
