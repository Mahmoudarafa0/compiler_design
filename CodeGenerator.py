from ply import lex, yacc

tokens = (
    'IF', 'ELSE', 'EQUALS', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS_EQUALS',
    'NOT_EQUALS', 'AND', 'OR', 'SEMICOLON'
)

t_IF = r'if'
t_ELSE = r'else'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'else':
        t.type = 'ELSE'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parsing rules
def p_statement(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
                | ID EQUALS expression SEMICOLON'''
    pass  # You can add the logic here

def p_condition(p):
    '''condition : expression EQUALS_EQUALS expression
                | expression NOT_EQUALS expression
                | expression AND expression
                | expression OR expression'''
    pass  # You can add the logic here

def p_expression(p):
    '''expression : term
                | term PLUS term
                | term MINUS term'''
    pass  # You can add the logic here

def p_term(p):
    '''term : factor
            | factor TIMES factor
            | factor DIVIDE factor'''
    pass  # You can add the logic here

def p_factor(p):
    '''factor : ID
            | NUM
            | LPAREN expression RPAREN'''
    pass  # You can add the logic here

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

data = "your_input_code_here"
lexer.input(data)
for token in lexer:
    print(token)

result = parser.parse(data)
