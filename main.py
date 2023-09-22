from lib.tokenizer import *
from lib.tokens_to_asm import *
from lib.info import *
import sys, os
from sys import exit

print()
try:
    path = sys.argv[1]
except Exception as e:
    print("Invalid usage")
    print("Correct usage: nebula <input>")
    print(f"Exception caught: {e}")
    exit(1)

if path != "--version":
    name = path.split("\\")[len(path.split("\\")) - 1]
    name = name.split("/")[len(name.split("/")) - 1]
    name = name.split(".")[0]
    file = open(path)
    if not os.path.exists("build"):
        os.mkdir("build")
    print(f"Building {sys.argv[1]}")
    with open(f"build\\{name}.asm", "w") as f:
        tokens = tokenize(file.read())
        #print(*tokens)
        asm = tokens_to_asm(tokens)
        f.write(asm)

    print()
    os.system(f"call buildasm.bat build\\{name}.asm {name}")
    print(f"Executable uses {os.stat(f'./build/{name}/{name}.exe').st_size} bytes")
else:
    print(f"Nebula version {VERSION}")
    print(f"Built on {BUILD_DATE}")
    print()