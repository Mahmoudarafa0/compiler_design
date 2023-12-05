import nltk
import re

input = open('InputProgram.c', 'r')
program = input.read()


keywords = []
identifiers = []
header_files = []
symbols = []
numerals = []
operators = []
string_literals = []

# removing spaces from the code
def remove_Spaces(program):
    scanned_Program = []
    for line in program:
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

# remove comments from the code
def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed

# Define regular expressions for different token types
c_keywords = ['include', 'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
keywords_pattern  = r'\b(?:' + '|'.join(c_keywords) + r')\b'

identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'

header_file_pattern = r'[a-zA-Z]+\.[h]'

symbol_pattern = r'[\[\]{}(),;.]'

numeral_pattern = r'\b(?:\d+\.\d*|\.\d+|\d+)\b'

c_operators = ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
operators_pattern = '|'.join(re.escape(op) for op in c_operators)

string_literal_pattern = r'"(?:\\.|[^"])*"'

pattern = f'{keywords_pattern}|{identifier_pattern}|{symbol_pattern}|{string_literal_pattern}|{operators_pattern}|{header_file_pattern}|{numeral_pattern}'


scanned_program = remove_Spaces(remove_Comments(program).split('\n')) # program after removing spaces and comments

# tokenize the program
for line in scanned_program:
    if(line.startswith("#include")):
        tokens = nltk.word_tokenize(line)
    elif(line.find("main()") != -1):
        tokens = nltk.word_tokenize(line)
    elif(line.find("printf") != -1):
        tokens = re.findall(pattern, line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    # inserting different tokens to lists
    for token in tokens:
        if(re.findall(keywords_pattern, token)):
            keywords.append(token)
        elif(re.findall(header_file_pattern,token)):
            header_files.append(token)
        elif(re.findall(string_literal_pattern, token)):
            string_literals.append(token)
        elif(re.findall(operators_pattern, token)):
            operators.append(token)
        elif(re.findall(numeral_pattern,token)):
            numerals.append(token)
        elif(re.findall(symbol_pattern, token)):
            symbols.append(token)
        elif(re.findall(identifier_pattern, token)):
            identifiers.append(token)

counter = len(keywords) + len(identifiers) + len(header_files) + len(symbols) + len(numerals) + len(operators) + len(string_literals)

output = open('Tokens.txt', 'w')
output.write(f"there are {counter} tokens\n")
output.write(f"There Are {len(keywords)} Keywords: {keywords}\n")
output.write(f"There Are {len(identifiers)} Identifiers: {identifiers}\n")
output.write(f"There Are {len(header_files)} Header Files: {header_files}\n")
output.write(f"There Are {len(symbols)} Symbols: {symbols}\n")
output.write(f"There Are {len(numerals)} Numerals: {numerals}\n")
output.write(f"There Are {len(operators)} Operators: {operators}\n")
output.write(f"There Are {len(string_literals)} string_literals: {string_literals}")

input.close()
output.close()