
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD_IDEA ADD_MEMBER ADD_TASK ASSIGN_TASK COMMA COMMAND COMPLETED_TASK CREATE_BRAINSTORM CREATE_GRAPH DATE DELETE_IDEA DELETE_MEMBER DELETE_TASK EDIT_TASK GENERATE_PROJECT GRAPH_AXIS GRAPH_DATA GRAPH_TYPE LIST_OVERDUE LIST_TODAY LIST_WEEK LPAREN NAME NAMELIST NEW_PROJECT NUMBER NUMBERLIST PHRASE RPAREN USERNAME VIEW_BRAINSTORM VIEW_MEMBERS VIEW_SCHEDULE VIEW_TASKS\n    statement : command PHRASE\n                | command PHRASE DATE DATE NUMBER\n                | command NUMBER DATE DATE NUMBER\n                | command PHRASE NUMBER\n                | command NUMBER\n                | command NUMBER NUMBER\n    \n    command : COMMAND\n    '
    
_lr_action_items = {'DATE':([4,5,6,9,],[6,9,10,11,]),'$end':([2,4,5,7,8,12,13,],[0,-5,-1,-6,-4,-3,-2,]),'PHRASE':([1,3,],[-7,5,]),'COMMAND':([0,],[1,]),'NUMBER':([1,3,4,5,10,11,],[-7,4,7,8,12,13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[2,]),'command':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> command PHRASE','statement',2,'p_statement','Parser.py',9),
  ('statement -> command PHRASE DATE DATE NUMBER','statement',5,'p_statement','Parser.py',10),
  ('statement -> command NUMBER DATE DATE NUMBER','statement',5,'p_statement','Parser.py',11),
  ('statement -> command PHRASE NUMBER','statement',3,'p_statement','Parser.py',12),
  ('statement -> command NUMBER','statement',2,'p_statement','Parser.py',13),
  ('statement -> command NUMBER NUMBER','statement',3,'p_statement','Parser.py',14),
  ('command -> COMMAND','command',1,'p_command','Parser.py',76),
]
