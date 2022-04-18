from collections import deque

# https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/100%20Bottom-Up%20Parsing.pdf
# grammar rules in reverse order
grammar_rules = {
    "E": "S",
    "T": "E",
    "E+T": "E",
    "id": "T",
    "(E)": "T"
}

initial_string = "int+(int+int+int)"


def parser(grammar_rules, parse_string):
    applied_grammar = []
    stack = deque([])
