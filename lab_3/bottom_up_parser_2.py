from collections import deque

# https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/100%20Bottom-Up%20Parsing.pdf
# grammar rules in reverse order
# grammar = {
#     "E0": "T",   # 0 E -> T
#     "E1": "E+T",  # 1 E -> E+T
#     "T0": "f",   # 2 T -> f
#     "T1": "T*f",  # 3 T -> T*f
#     "f1": "(E)",  # 4 f -> (E)
#     "f0": "x",   # 5 f -> x
# }

grammar = {
    "E+T": "E",
    "T": "E",
    "T*F": "T",
    "F": "T",
    "(E)": "F",
    "x": "F"
}

table_column_pos = {
    'E': 0,
    'T': 1,
    'F': 2,
    '+': 3,
    '*': 4,
    '(': 5,
    ')': 6,
    'x': 7,
    '@': 8,
}

table = [
    ['empty string']
    ["S2", "S5", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "S3", "", "", "", "", ""],
    ["", "S4", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "R1", "S6", "", "R1", "", "R1"],
    ["", "", "", "R2", "S6", "", "R2", "", "R2"],
    ["", "", "S7", "", "", "S9", "", "S12", ""],
    ["R3", "R3", "R3", "R3", "R3", "R3", "R3", "R3", "R3"],
    ["R4", "R4", "R4", "R4", "R4", "R4", "R4", "R4", "R4"],
    ["S10", "S5", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "S3", "", "", "S11", "", ""],
    ["R5", "R5", "R5", "R5", "R5", "R5", "R5", "R5", "R5"],
    ["R6", "R6", "R6", "R6", "R6", "R6", "R6", "R6", "R6"],
]


class BottomUpParser:
    def __init__(self, expression):
        self.expression = f"{expression}@"
        self.exp_pos = 0

    def analase(self):
        state_stack = [1]
        char_stack = [self.expression[self.exp_pos]]
        syntax_form = f"{self.expression}"


parser = BottomUpParser("x+(x+x)*x")
parser.analase()
