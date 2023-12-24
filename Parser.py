from LexicalAnalyzer import identifier_pattern, numeral_pattern
import re
from LexicalAnalyzer import output_tokens as tokens

# this is a rule for the statement pattern
def statement():
  global token
  if (token == 'if'):
    match('if')
    match('(')
    condition()
    match(')')
    match('{')
    statement()
    match('}')
    if (token == 'else'):
      match('else')
      match('{')
      statement()
      match('}')
  elif (re.match(identifier_pattern, token)):
    match(token)
    match('=')
    expression()
    match(';')
  else:
    print(f"syntax error: unexpected token {token}")
    exit()

# this function for matching the current token with the expected
def match(expected):
  global token
  if (token == expected):
    print(token)
    if (len(tokens) == 0):
      print('accepted')
      exit()
    token = tokens.pop(0)
  else:
    print(f"syntax error: expected {expected} but got {token}")
    exit()

# this is a rule for the condition pattern
def condition():
  global token
  expression()
  if (token == '==' or token == '!=' or token == '&&' or token == '||'):
    print(token)
    if (len(tokens) == 0):
      print('accepted')
      exit()
    token = tokens.pop(0)
    expression()

# this is a rule for the expression pattern
def expression():
  global token
  term()
  while token in ['+', '-', '*', '/']:
    print(token)
    if (len(tokens) == 0):
      print('accepted')
      exit()
    token = tokens.pop(0)
    term()

# this is a rule for the tearm pattern
def term():
  global token
  factor()
  while token in ['+', '-', '*', '/']:
    print(token)
    if (len(tokens) == 0):
      print('accepted')
      exit()
    token = tokens.pop(0)
    factor()

# this is a rule for the factor pattern
def factor():
  global token
  if (re.match(identifier_pattern, token) or re.match(numeral_pattern, token)):
    print(token)
    if (len(tokens) == 0):
      print('accepted')
      exit()
    token = tokens.pop(0)
  elif (token == '('):
    match('(')
    expression()
    match(')')
  else:
    print(f"syntax error: unexpected token {token}")
    exit()


token = tokens.pop(0)
statement()