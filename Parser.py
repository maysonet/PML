import Utils
import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

#Parsing Rules
def p_statement(p):
    """
    statement : create_project
            | add_member
            | add_brainstorm
            | add_idea
            | add_task
            | view_members
            | view_tasks
            | view_brainstorm
            | view_schedule
            | view_today
            | view_week
            | view_overdue
            | delete_member
            | delete_task
            | complete_task
            | edit_task
            | assign_task
            | generate_project
            | generate_pie
            | generate_bar



    """
    p[0] = p[1]
    pass


def p_create_project(p):
    'create_project : NEW_PROJECT PHRASE'
    # New_project << project_name >>
    Utils.new_project(p[2])


def p_add_member(p):
    """
    add_member : ADD_MEMBER PHRASE NUMBER
    """
    # Add_member << member_name >> << project_id >>
    Utils.add_user(p[2], p[3])

def p_add_brainstorm(p):
    """
    add_brainstorm : CREATE_BRAINSTORM PHRASE NUMBER
    """
    # create_brainstorm << main_topic >> << project_id >>
    Utils.add_brainstorm(p[2], p[3])

def p_add_idea(p):
    """
    add_idea : ADD_IDEA PHRASE NUMBER
    """
    # add_idea <<idea_name>> <<project_id>>
    Utils.add_idea(p[2], p[3])

def p_view_members(p):
    """
    view_members : VIEW_MEMBERS NUMBER
    """
    # view_members <<project_id>>
    Utils.view_members(p[2])

def p_view_tasks(p):
    """
    view_tasks : VIEW_TASKS NUMBER
    """
    # view_tasks <<project_id>>
    Utils.view_tasks(p[2])

def p_view_brainstorm(p):
    """
    view_brainstorm : VIEW_BRAINSTORM NUMBER
    """
    # view_brainstorm <<project_id>>
    Utils.generate_diagram(p[2])

def p_view_schedule(p):
    """
    view_schedule : VIEW_SCHEDULE NUMBER
    """
    # view_schedule <<project_id>>
    Utils.generate_gantt(p[2])

def p_view_today(p):
    """
    view_today : LIST_TODAY NUMBER
    """
    # list_today <<project_id>>
    Utils.view_today(p[2])

def p_view_week(p):
    """
    view_week : LIST_WEEK NUMBER
    """
    # list_week <<project_id>>
    Utils.view_week(p[2])

def p_view_overdue(p):
    """
    view_overdue : LIST_OVERDUE NUMBER
    """
    # list_overdue <<project_id>>
    Utils.view_overdue(p[2])

def p_delete_member(p):
    """
    delete_member : DELETE_MEMBER NUMBER NUMBER
    """
    # Delete_member << member_id >> <<project_id>>
    Utils.remove_user(p[2], p[3])

def p_delete_task(p):
    """
    delete_task : DELETE_TASK NUMBER NUMBER
    """
    # Delete_task << task_id >> <<project_id>>
    Utils.remove_task(p[2], p[3])

def p_complete_task(p):
    """
    complete_task : COMPLETED_TASK NUMBER NUMBER
    """
    # completed_task << task_id >> <<project_id>>
    Utils.completed_task(p[2], p[3])

def p_add_task(p):
    """
    add_task : ADD_TASK PHRASE DATE DATE NUMBER
    """
    # Add_task <<task_name>> <<start_date>> <<finish_date>> <<project_id>>
    Utils.add_task(p[2], p[3], p[4], p[5])

def p_edit_task(p):
    """
    edit_task : EDIT_TASK NUMBER DATE DATE NUMBER
    """
    # Edit_task <<task_id>> <<start_date>> <<finish_date>> <<project_id>>
    Utils.edit_task(p[2], p[3], p[4], p[5])

def p_assign_task(p):
    """
    assign_task : ASSIGN_TASK NUMBER NUMBER NUMBER
    """
    # Assign_task <<task_id>> <<member_id>> <<project_id>>
    Utils.assign_task(p[2], p[3], p[4])

def p_generate_project(p):
    """
    generate_project : GENERATE_PROJECT NUMBER
    """
    # generate_project <<project_id>>
    Utils.generate_project(p[2])

def p_generate_pie(p):
    """
    generate_pie : GENERATE_PIE NAMELIST NUMBERLIST
    """
    # generate_project <<project_id>>
    Utils.generate_pie(p[2], p[3])

def p_generate_bar(p):
    """
    generate_bar : GENERATE_BAR NAMELIST NUMBERLIST
    """
    # generate_project <<project_id>>
    Utils.generate_bar(p[2], p[3])

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
    elif s == 'exit':
        break
    try:
        parser.parse(s)
    except SyntaxError:
        print('Invalid syntax')
