import sys
class StringBuffer:
    def __init__(self, default_val : str = "", push_start : str = "", push_end : str = ""):
        self._str_ = default_val
        self.push_start = push_start
        self.push_end = push_end
    def push(self, string : str):
        self._str_ += self.push_start + string + self.push_end
    def __str__(self) -> str:
        return self._str_
    def get(self) -> str:
        return self._str_
def ProgressBar(name, value, endvalue, bar_length = 50, width = 20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent*bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        sys.stdout.write("\r{0: <{1}} : [{2}]{3}%".format(\
                         name, width, arrow + spaces, int(round(percent*100))))
        sys.stdout.flush()
        if value == endvalue:     
             sys.stdout.write('\n')