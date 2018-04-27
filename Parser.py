import Utils
import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

#Parsing Rules
def p_statement(p):

    """
    statement : command PHRASE
                | command PHRASE DATE DATE NUMBER
                | command PHRASE NUMBER
                | command NUMBER
    """
    try:
        if p[1] == 'NEW_PROJECT':
            Utils.new_project(p[2])
            # OR we can just accept project name and let the system assign ID
            # Need to fix input rules so that SPACES are allowed in Project name
        if p[1] == 'NEW_MEMBER':
            Utils.add_user(p[2], p[3])
        if p[1] == 'ADD_TASK':
            Utils.add_task(p[2], p[3], p[4], p[5])
            # Need to fix input rules so that SPACES are allowed in task description

        if p[1] == 'CREATE_BRAINSTORM':
            Utils.add_brainstorm(p[2], p[3])

        if p[1] == 'ADD_IDEA':
            Utils.add_idea(p[2], p[3])

        if p[1] == 'VIEW_BRAINSTORM':
            Utils.generate_diagram(p[2])

        #The following NEED to be IMPLEMENTED in LEXER and UTILS
        if p[1] == 'VIEW_GANTT':
            pass
        if p[1] == 'LIST_TODAY':
            pass
        if p[1] == 'LIST_WEEK':
            pass


    except:
        print('Invalid Parameters')


def p_command(p):
    """
    command : COMMAND
    """
    p[0] = p[1]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
while 1:
    try:
        s = input('PML > ')
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
