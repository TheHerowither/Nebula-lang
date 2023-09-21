from enum import Enum
from lib.qol_classes import *
from lib.errors import *
from sys import exit


class TokenType(Enum):
    Semi = ";"
    IntLit = "0123456789"
    Return = "return"
    VarDecl = "set"
    VarName = ""
    Equ = "="
    Print = "print"
    Comm = "//"
    Add = "+"
class Token:
    def __init__(self, type : TokenType, value : str = None):
        self.type = type
        self.value = value
    def __str__(self):
        return f"Token(.type = {self.type.name}, .value = {self.value})"

def tokenize(contents : str) -> list[Token]:
    c = contents
    lines = c.split("\n")
    tokens = []
    line_nmbr = 0
    variabels = []
    
    while line_nmbr <= len(lines) - 1:
        ProgressBar("Tokenizing", line_nmbr, len(lines))
        line = lines[line_nmbr]
        column_nmbr = 0
        while column_nmbr <= len(line) - 1:
            char = line[column_nmbr]
            while char == "/":
                if line[column_nmbr+1] == "/":
                    line_nmbr += 1
                    line = lines[line_nmbr]
                    char = line[column_nmbr]
                else:
                    break
            if char.isalnum():
                
                if char.isalpha():
                    buf = StringBuffer()
                    while char.isalpha():
                        buf.push(char)
                        try:
                            column_nmbr += 1
                            char = line[column_nmbr]
                        except:
                            break
                    #Check for keywords
                    if buf.get() == "return":
                        tokens.append(Token(TokenType.Return))
                    elif buf.get() == "set":
                        tokens.append(Token(TokenType.VarDecl))
                        buf = StringBuffer()
                        try:
                            column_nmbr += 1
                            char = line[column_nmbr]
                        except:
                            pass
                        while char.isalpha():
                            buf.push(char)
                            try:
                                column_nmbr += 1
                                char = line[column_nmbr]
                            except:
                                break
                        tokens.append(Token(TokenType.VarName, buf.get()))
                        variabels.append(buf.get())
                    elif buf.get() == "print":
                        tokens.append(Token(TokenType.Print, None))
                    elif buf.get() in variabels:
                        tokens.append(Token(TokenType.VarName, buf.get()))
                        
                    elif char.isspace():
                        continue
                    else:
                        print(f"\nInvalid syntax, at line {line_nmbr + 1}, column {column_nmbr + 1}")
                        print(f"Found {buf.get()}")
                        exit(1)
                elif char.isnumeric():
                    buf = StringBuffer()
                    while char.isnumeric():
                        buf.push(char)
                        try:
                            column_nmbr += 1
                            char = line[column_nmbr]
                        except:
                            break
                    tokens.append(Token(TokenType.IntLit, buf._str_))
            if char.isspace():
                pass
            elif char == ";":
                tokens.append(Token(TokenType.Semi))
                try:
                    column_nmbr += 1
                    char = line[column_nmbr]
                except: pass
            elif char == "=":
                tokens.append(Token(TokenType.Equ))
                try:
                    column_nmbr += 1
                    char = line[column_nmbr]
                except: pass
            elif char == "+":
                tokens.append(Token(TokenType.Add))
                try:
                    column_nmbr += 1
                    char = line[column_nmbr]
                except: pass
            else:
                print(f"\nInvalid syntax, at line {line_nmbr + 1}, column {column_nmbr + 1}")
                print(f"Found {buf.get()}")
                exit(1)
            column_nmbr += 1
        line_nmbr += 1
        ProgressBar("Tokenizing", line_nmbr, len(lines))
    return tokens