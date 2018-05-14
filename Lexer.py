import ply.lex as lex

# Reserved Words
reserved = {
    'new_project': 'NEW_PROJECT', #Done
    'add_member': 'ADD_MEMBER', #Done
    'delete_member' : 'DELETE_MEMBER', #Done
    'view_members' : 'VIEW_MEMBERS', ##Done
    'create_brainstorm':'CREATE_BRAINSTORM', #Done
    'add_idea':'ADD_IDEA', #Done
    'delete_idea':'DELETE_IDEA', #No esta en la lista
    'add_task': 'ADD_TASK', #Done
    'edit_task': 'EDIT_TASK', #####Falta
    'delete_task': 'DELETE_TASK', ##Done
    'completed_task': 'COMPLETED_TASK', ##Done
    'assign_task': 'ASSIGN_TASK', #####Falta
    'create_graph': 'CREATE_GRAPH', ## Mikael
    'graph_type':'GRAPH_TYPE', # Mikael
    'graph_axis':'GRAPH_AXIS', # Mikael
    'graph_data' : 'GRAPH_DATA', # Mikael
    'view_brainstorm':'VIEW_BRAINSTORM', #Done
    'view_schedule': 'VIEW_SCHEDULE', #Done
    'view_tasks' : 'VIEW_TASKS', ##Done
    'list_today' : 'LIST_TODAY', #####Falta
    'list_week' : 'LIST_WEEK', #####Falta
    'list_overdue' : 'LIST_OVERDUE', #####Falta
    'generate_project' : 'GENERATE_PROJECT' #####Falta
}

# Tokens
tokens = ["NAME",
          "USERNAME",
          "DATE",
          "NUMBER",
          "PHRASE",
          "NUMBERLIST",
          "NAMELIST",
          'LPAREN', 'RPAREN', 'COMMA',
          "COMMAND"] \
         + list(reserved.values())

# Simple Regular Expressions
t_ignore = ' \t'
t_USERNAME = r'@[a-zA-Z]+'
t_NAME = r'[a-zA-Z]+'
t_PHRASE = r'[a-zA-Z ]+'
t_NUMBER = r'[\d+]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_COMMAND = r'[a-zA-Z]+_[a-zA-Z]+'
## NEED regular expression to accept characters and spaces - for tasks

#date format: 2012-02-20 -- year-month-day
#t_DATE = r'\d+-\d+-\d+'
t_DATE = r'[0-9]{2}'+r'-'+r'[0-9]{2}'+r'-'+r'[0-9]{4}'

# Regular expression for list of numbers
def t_LIST(t):
    r'[(][-?0-9,]+[-?0-9][)]'
    t.type = 'NUMBERLIST'
    return t
# Regular expression for list of words
def t_LIST2(t):
    r'[(][\'a-zA-z\']+[,\'a-zA-Z\']*[)]'
    t.type = 'NAMELIST'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Test it out
data0 = '''graph_data (woo,goo,joo) (12,-14,16)'''
data1 = '''new_member member Name project Name'''
data2 = '''delete_member @member  project Name'''
data3 = '''create_brainstorm brainstorn Name '''
#data1 = 2012-02-20 2012-02-26

# Give the lexer some input
lexer.input(data0)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
