import Utils
import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

#Parsing Rules
def p_statement(p):

    """
    statement : command PHRASE
                | command PHRASE DATE DATE NUMBER
                | command NUMBER DATE DATE NUMBER
                | command PHRASE NUMBER
                | command NUMBER
                | command NUMBER NUMBER
                | command NUMBER NUMBER NUMBER
    """
    try:
        # New_project << project_name >>
        if p[1] == 'NEW_PROJECT':
            Utils.new_project(p[2])
            # OR we can just accept project name and let the system assign ID
            # Need to fix input rules so that SPACES are allowed in Project name

        # Add_member << member_name >> << project_id >>
        if p[1] == 'ADD_MEMBER':
            Utils.add_user(p[2], p[3])

        # Delete_member << member_id >> <<project_id>>
        if p[1] == 'DELETE_MEMBER':
            Utils.remove_user(p[2], p[3])

        # View_members <<project_id>>
        if p[1] == 'VIEW_MEMBERS':
            Utils.view_members(p[2])

        # Add_task <<task_name>> <<start_date>> <<finish_date>> <<project_id>>
        if p[1] == 'ADD_TASK':
            Utils.add_task(p[2], p[3], p[4], p[5])
            # Need to fix input rules so that SPACES are allowed in task description

        # Delete_task << task_id >> <<project_id>>
        if p[1] == 'DELETE_TASK':
            #Hay que hacerle test
            Utils.remove_task(p[2], p[3])

        # Edit_task <<task_id>> <<start_date>> <<finish_date>> <<project_id>>
        if p[1] == 'EDIT_TASK':
            Utils.edit_task(p[2], p[3], p[4], p[5])

        # Completed_task <<task_id>> <<project_id>>
        if p[1] == 'COMPLETED_TASK':
            Utils.completed_task(p[2], p[3])

        # Assign_task <<task_id>> <<member_id>> <<project_id>>
        if p[1] == 'ASSIGN_TASK':
            Utils.assign_task(p[2], p[3], p[4])

        # view_tasks <<project_id>>
        if p[1] == 'VIEW_TASKS':
            Utils.view_tasks(p[2])

        if p[1] == 'CREATE_BRAINSTORM':
            Utils.add_brainstorm(p[2], p[3])

        if p[1] == 'ADD_IDEA':
            Utils.add_idea(p[2], p[3])

        if p[1] == 'VIEW_BRAINSTORM':
            Utils.generate_diagram(p[2])

        #The following NEED to be IMPLEMENTED in LEXER and UTILS
        if p[1] == 'VIEW_SCHEDULE':
            Utils.generate_gantt(p[2])
        if p[1] == 'LIST_TODAY':
            Utils.view_today(p[2])
        if p[1] == 'LIST_WEEK':
            Utils.view_week(p[2])
        if p[1] == 'LIST_OVERDUE':
            Utils.view_overdue(p[2])

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
