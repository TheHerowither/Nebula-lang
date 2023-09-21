from lib.tokenizer import Token, TokenType
from lib.assembly import Assembly
from lib.qol_classes import ProgressBar
from sys import exit


def tokens_to_asm(tokens : list[Token],int_bytes : int = 4):
    asm = Assembly()
    asm.extern("_ExitProcess@4")
    asm.section("text")
    
    asm.Global("_start")

    asm.write_to_section("_start", "push ebp")
    asm.write_to_section("_start", "mov ebp, esp")
    _vars = 0
    var_index = {}
    for token in tokens:
        ProgressBar("Converting to assembly", tokens.index(token), len(tokens))
        if token.type == TokenType.Return:
            if tokens[tokens.index(token) + 1].type == TokenType.IntLit:
                try:
                    if tokens[tokens.index(token) + 2].type == TokenType.Semi:
                        asm.write_to_section("_start", f"push {tokens[tokens.index(token) + 1].value}")
                        asm.write_to_section("_start", "call _ExitProcess@4")
                    else:
                        print("\nYou messed up")
                        print(f"Expected ';' found {tokens[tokens.index(token) + 2].type.name}")
                        exit(1)
                except IndexError:
                    print("\nYou messed up")
                    print("Excpected ';'")
                    exit(1)
            elif tokens[tokens.index(token) + 1].type == TokenType.VarName:
                try:
                    if tokens[tokens.index(token) + 2].type == TokenType.Semi:
                        asm.write_to_section("_start", f"mov eax, [ebp-{var_index[tokens[tokens.index(token) + 1].value]}]")
                        asm.write_to_section("_start", f"push eax")
                        asm.write_to_section("_start", "call _ExitProcess@4")
                    else:
                        print("\nYou messed up")
                        print(f"Expected ';' found {tokens[tokens.index(token) + 2].type.name}")
                        exit(1)
                except IndexError:
                    print("\nYou messed up")
                    print("Excpected ';'")
                    exit(1)
        if token.type == TokenType.VarDecl:
            if tokens[tokens.index(token) + 1].type == TokenType.VarName:
                if tokens[tokens.index(token) + 2].type == TokenType.Equ:
                    if tokens[tokens.index(token) + 3].type == TokenType.IntLit:
                        if tokens[tokens.index(token) + 4].type == TokenType.Semi:
                            asm.write_to_section("_start", f"sub esp, {int_bytes * (_vars + 1)}")
                            asm.write_to_section("_start", f"mov dword [ebp-{int_bytes * (_vars + 1)}], {tokens[tokens.index(token) + 3].value}")
                            asm.write_to_section("_start", f"mov eax, [ebp-{int_bytes * (_vars + 1)}]")
                            var_index[tokens[tokens.index(token) + 1].value] = int_bytes * (_vars + 1)
                            _vars += 1

    try:ProgressBar("Converting to assembly", len(tokens), len(tokens))
    except:pass
    
    return asm.to_asm()