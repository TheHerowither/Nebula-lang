from lib.qol_classes import StringBuffer



class AssemblyCode:
    def __init__(self):
        self.lines = []
        self.labels = {}
        self.vars = {}
    def add_line(self, string : str, line : int):
        if line != -1:
            bottom = [self.lines[ln:ln+line] for ln in range(0, len(self.lines), line + 1)]
            try:
                [self.lines.pop(self.lines.index(self.lines[ln:ln+line])) for ln in range(0, len(self.lines), line + 1)]
                self.lines.append(string)
                [self.lines.append(i) for i in bottom]
            except ValueError: pass
        else:
            self.lines.append(string)
    def add_label(self, label_name : str, label_content = list[str]):
        self.labels[f"{label_name}:"] = label_content
    def add_to_label(self, label_name : str, content : str):
        self.labels[f"{label_name}:"].append(content)
    def to_string(self) -> str:
        buf = StringBuffer(push_end="\n")
        for line in self.lines:
            buf.push(line)
        for lineb in self.labels.keys():
            buf.push(lineb)
            for content in self.labels[lineb]:
                buf.push(f"    {content}")
        return buf.get().strip()
class Assembly:
    def __init__(self):
        self.code = AssemblyCode()
        self.code.add_label("_start", [])
        self.globals = 0
    def extern(self, name : str):
        self.code.add_line(f"extern {name}", -1)
    def Global(self, section_name : str):
        self.code.add_line(f"   global {section_name}", -1)
        self.globals += 1
    def section(self, name : str):
        self.code.add_line(f"section .{name}", -1)
    def label(self, name : str):
        self.code.add_label(name, [])
    def write_to_section(self, label : str, content : str):
        self.code.add_to_label(label, content)
    def to_asm(self) -> str:
        return self.code.to_string()
    def add_variable(self, var_name, var_val, type = "DW", extra = ""):
        self.code.vars[var_name] = [var_val, type, extra]
    def call(self, label : str):
        self.code.add_line(f"call {label}", -1)