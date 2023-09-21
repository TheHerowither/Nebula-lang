from lib.tokenizer import *
from lib.tokens_to_asm import *
import sys, os
from sys import exit

print()
try:
    file = open(sys.argv[1])
except Exception as e:
    print("Invalid usage")
    print("Correct usage: nebula <input>")
    print(f"Exception caught: {e}")
    exit(1)

if not os.path.exists("build"):
    os.mkdir("build")
print(f"Building {sys.argv[1]}")
with open("build\\main.asm", "w") as f:
    tokens = tokenize(file.read())
    #print(*tokens)
    asm = tokens_to_asm(tokens)
    f.write(asm)

print()
os.system("call buildasm.bat build\\main.asm")
print(f"Executable uses {os.stat('./build/main.exe').st_size} bytes")