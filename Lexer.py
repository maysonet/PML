import ply.lex as lex

# Reserved Words
reserved = {
    'new_project': 'NEW_PROJECT', #Done
    'add_member': 'ADD_MEMBER', #Done
    'delete_member' : 'DELETE_MEMBER', #Done
    'view_members' : 'VIEW_MEMBERS', #Done
    'create_brainstorm':'CREATE_BRAINSTORM', #Done
    'add_idea':'ADD_IDEA', #Done
    'add_task': 'ADD_TASK', #Done
    'edit_task': 'EDIT_TASK', #Done
    'delete_task': 'DELETE_TASK', #Done
    'completed_task': 'COMPLETED_TASK', #Done
    'assign_task': 'ASSIGN_TASK', #Done
    'view_brainstorm':'VIEW_BRAINSTORM', #Done
    'view_schedule': 'VIEW_SCHEDULE', #Done
    'view_tasks' : 'VIEW_TASKS', #Done
    'list_today' : 'LIST_TODAY', #Done
    'list_week' : 'LIST_WEEK', #Done
    'list_overdue' : 'LIST_OVERDUE', #Done
    'generate_project' : 'GENERATE_PROJECT', #Done
    'generate_pie' : 'GENERATE_PIE',
    'generate_bar' : 'GENERATE_BAR',
    'generate_line' : 'GENERATE_LINE'
}

# Tokens
tokens = ["NAME",
          "DATE",
          "NUMBER",
          "PHRASE",
          "NUMBERLIST",
          "NAMELIST",
          'LBRK', 'RBRK', 'COMMA',
          "ID"] + list(reserved.values())

# Simple Regular Expressions
t_ignore = ' \t'
t_NAME = r'[a-zA-Z]+'
t_PHRASE = r'[a-zA-Z ]+'
t_NUMBER = r'[\d+]+'
t_LBRK = r'\['
t_RBRK = r'\]'
t_COMMA = r'\,'
#t_COMMAND = r'[a-zA-Z]+_[a-zA-Z]+'
## NEED regular expression to accept characters and spaces - for tasks

# Define a rule for reserved words
def t_ID(t):
    r'[a-zA-Z]+_[a-zA-Z]+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

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
data0 = '''generate_line (woo) (wee) (12,-14,16) (12,12,12)'''
data1 = '''new_project member Name project Name'''
data2 = '''delete_member @member  project Name'''
data3 = '''create_brainstorm brainstorn Name '''
#data1 = 2012-02-20 2012-02-26

# Give the lexer some input
#lexer.input(data0)

# Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)
