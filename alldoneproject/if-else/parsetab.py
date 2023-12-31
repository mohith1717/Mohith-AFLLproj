
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN ELSE EQUALS GT ID IF LBRACE LPAREN NUMBER RBRACE RPAREN SEMICOLONstart : statementsstatements : statement statements\n                  | emptystatement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE\n                 | ID EQUALS expression SEMICOLONexpression : expression GT expression\n                  | BOOLEAN\n                  | IDempty :'
    
_lr_action_items = {'IF':([0,3,16,17,22,24,],[5,5,-5,5,5,-4,]),'ID':([0,3,8,9,15,16,17,22,24,],[6,6,12,12,12,-5,6,6,-4,]),'$end':([0,1,2,3,4,7,16,24,],[-9,0,-1,-9,-3,-2,-5,-4,]),'RBRACE':([3,4,7,16,17,19,22,23,24,],[-9,-3,-2,-5,-9,20,-9,24,-4,]),'LPAREN':([5,],[8,]),'EQUALS':([6,],[9,]),'BOOLEAN':([8,9,15,],[11,11,11,]),'RPAREN':([10,11,12,18,],[14,-7,-8,-6,]),'GT':([10,11,12,13,18,],[15,-7,-8,15,15,]),'SEMICOLON':([11,12,13,18,],[-7,-8,16,-6,]),'LBRACE':([14,21,],[17,22,]),'ELSE':([20,],[21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statements':([0,3,17,22,],[2,7,19,23,]),'statement':([0,3,17,22,],[3,3,3,3,]),'empty':([0,3,17,22,],[4,4,4,4,]),'expression':([8,9,15,],[10,13,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statements','start',1,'p_start','parser_1.py',6),
  ('statements -> statement statements','statements',2,'p_statements','parser_1.py',10),
  ('statements -> empty','statements',1,'p_statements','parser_1.py',11),
  ('statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE','statement',11,'p_statement','parser_1.py',15),
  ('statement -> ID EQUALS expression SEMICOLON','statement',4,'p_statement','parser_1.py',16),
  ('expression -> expression GT expression','expression',3,'p_expression','parser_1.py',20),
  ('expression -> BOOLEAN','expression',1,'p_expression','parser_1.py',21),
  ('expression -> ID','expression',1,'p_expression','parser_1.py',22),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',26),
]
