from sys import exit
def syntax_error(line, column):
    print(f"Syntax error at line {line}, column {column}")
    exit(1)