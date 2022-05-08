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

grammar_pos = [
    [],
    ["E+T", "E"],
    ["T", "E"],
    ["T*F", "T"],
    ["F", "T"],
    ["(E)", "F"],
    ["x", "F"],
]


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
    # ['empty string'],
    # ["S2", "S5", "S8", "", "", "S9", "", "S12", ""],
    # ["", "", "", "S3", "", "", "", "", ""],
    # ["", "S4", "S8", "", "", "S9", "", "S12", ""],
    # ["", "", "", "R1", "S6", "", "R1", "", "R1"],
    # ["", "", "", "R2", "S6", "", "R2", "", "R2"],
    # ["", "", "S7", "", "", "S9", "", "S12", ""],
    # ["R3", "R3", "R3", "R3", "R3", "R3", "R3", "R3", "R3"],
    # ["R4", "R4", "R4", "R4", "R4", "R4", "R4", "R4", "R4"],
    # ["S10", "S5", "S8", "", "", "S9", "", "S12", ""],
    # ["", "", "", "S3", "", "", "S11", "", ""],
    # ["R5", "R5", "R5", "R5", "R5", "R5", "R5", "R5", "R5"],
    # ["R6", "R6", "R6", "R6", "R6", "R6", "R6", "R6", "R6"],
    ['empty string'],
    ["S2", "S5", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "S3", "", "", "", "", ""],
    ["", "S4", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "R1", "S6", "", "R1", "", "R1"],
    ["", "", "", "R2", "S6", "", "R2", "", "R2"],
    ["", "", "S7", "", "", "S9", "", "S12", ""],
    ["", "", "", "R3", "R3", "", "R3", "", "R3"],
    ["", "", "", "R4", "R4", "", "R4", "", "R4"],
    ["S10", "S5", "S8", "", "", "S9", "", "S12", ""],
    ["", "", "", "S3", "", "", "S11", "", ""],
    ["", "", "", "R5", "R5", "", "R5", "", "R5"],
    ["", "", "", "R6", "R6", "", "R6", "", "R6"],
]


class BottomUpParser:
    def __init__(self, expression):
        self.expression = f"{expression}@"
        self.exp_pos = 0

    def analyse(self):
        # в начальный момент состояние 1
        state_stack = [1]
        # стек символов
        char_stack = []
        # итоговая форма которая у нас получается в процессе обработки
        syntax_form = f"{self.expression}"
        # сначала входной символ это первый символ строки
        input_char = self.expression[0]

        # считаем что введенная строка верная и поэтому выполняем код, пока она не станет
        # равной выражению
        while syntax_form != "E":
            # берем последнее состояние со стека
            last_state = state_stack.pop()

            # определяем свертку или сдвиг надо совершить
            col_pos = table_column_pos[input_char]
            action = table[last_state][col_pos]

            # сдвиг
            if "S" in action:
                # добавляем входной символ в стек символов
                char_stack.append(input_char)
                # берем номер состояния в которое нужно перейти
                action_state_num = int(action[1:])
                # добавляем его в стек состояний
                state_stack.append(action_state_num)
                # если входной символ является терминалом, то
                if input_char in "x()+*@":
                    self.exp_pos += 1
                    input_char = self.expression[self.exp_pos]
            # свертка
            elif "R" in action:
                # берем номер продукции
                grammar_index = int(action[1:])
                # берем саму продукцию по номеру
                rule = grammar_pos[grammar_index]
                # узнаем длину продукции
                rule_len = len(rule[0])
                # сокращаем стек символов на длину продукции
                char_stack = char_stack[:-rule_len]
                # сокращаем стек состояний на длину продукции
                state_stack = state_stack[:-rule_len]
                # берем саму продукцию, на которую нужно заменить терминал
                rule_production = rule[1]
                # добавляем продукцию с стек символов
                char_stack.append(rule_production)
                # добавляем номер продукции в стек состояний
                state_stack.append(grammar_index)
                # делаем продукцию входным символом
                input_char = rule_production

            # получаем итоговую строку путем соединения стека символов и оставшейся исходной строки
            syntax_form = f"{''.join(char_stack)}{self.expression[self.exp_pos:]}"


parser = BottomUpParser("x+(x+x)*x")
parser.analyse()
