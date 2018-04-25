
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DATE ID NAME NEW TASK USER\n    statement : command NAME ID\n                | command NAME DATE DATE\n                | command NAME\n    \n    command : NAME\n    '
    
_lr_action_items = {'NAME':([0,2,3,],[3,4,-4,]),'$end':([1,4,5,7,],[0,-3,-1,-2,]),'ID':([4,],[5,]),'DATE':([4,6,],[6,7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'command':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> command NAME ID','statement',3,'p_statement','Parser.py',10),
  ('statement -> command NAME DATE DATE','statement',4,'p_statement','Parser.py',11),
  ('statement -> command NAME','statement',2,'p_statement','Parser.py',12),
  ('command -> NAME','command',1,'p_command','Parser.py',32),
]
