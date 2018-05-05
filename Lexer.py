import ply.lex as lex

# Reserved Words
reserved = {
    'new_project': 'NEW_PROJECT',
    'add_member': 'ADD_MEMBER',
    'delete_member' : 'DELETE_MEMBER',
    'create_brainstorm':'CREATE_BRAINSTORM',
    'add_idea':'ADD_IDEA',
    'delete_idea':'DELETE_IDEA',
    'add_task': 'ADD_TASK',
    'edit_task': 'EDIT_TASK',
    'delete_task': 'DELETE_TASK',
    'assign_task': 'ASSIGN_TASK',
    'create_graph': 'CREATE_GRAPH',
    'graph_type':'GRAPH_TYPE',
    'graph_axis':'GRAPH_AXIS',
    'graph_data' : 'GRAPH_DATA',
    'view_brainstorm':'VIEW_BRAINSTORM',
    'view_schedule': 'VIEW_SCHEDULE',
    'view_tasks' : 'VIEW_TASKS',
    'list_today' : 'LIST_TODAY',
    'list_week' : 'LIST_WEEK',
    'list_overdue' : 'LIST_OVERDUE',
    'generate_project' : 'GENERATE_PROJECT'

}

# Tokens
tokens = ["NAME","USERNAME", "DATE", "NUMBER", "PHRASE", "COMMAND"] + list(reserved.values())

# Simple Regular Expressions
t_ignore = ' \t'
t_USERNAME = r'@[a-zA-Z]+'
t_NAME = r'[a-zA-Z]+'

t_PHRASE = r'[a-zA-Z ]+'
t_NUMBER = r'[\d+]+'
t_COMMAND = r'[a-zA-Z]+_[a-zA-Z]+'
## NEED regular expression to accept characters and spaces - for tasks

#date format: 2012-02-20 -- year-month-day
#t_DATE = r'\d+-\d+-\d+'
t_DATE = r'[0-9]{2}'+r'-'+r'[0-9]{2}'+r'-'+r'[0-9]{4}'

def t_error(t):
    print('Illegal character %s', t.value[0])
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

# Test it out
data0 = '''new_project project Name'''
data1 = '''new_member member Name project Name'''
data1 = '''delete_member @member  project Name'''
data2 = '''create_brainstorm brainstorn Name '''
#data1 = 2012-02-20 2012-02-26

# Give the lexer some input
lexer.input(data1)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
