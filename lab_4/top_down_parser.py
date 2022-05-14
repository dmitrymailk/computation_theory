"""
Top-down parser python 3 for grammar
E –> TE'
E'–> + TE' | ε
T –> FT'
T'–> * FT' | ε
F –> (E) | x
"""
from collections import deque


class SyntaxTable:
    def __init__(self) -> None:
        """
        ε в книге и теории должны быть заменены на просто на отсутствие строки.
        Так в процессе добавления правила мы добавим пустой массив слева и поэтому
        никак не изменим стек
        Пример
        В книге имее правило типа T' → ε
        В коде заменяем на ["T'", тут ничего не должно быть]
        """

        self.table = [
            [["E", "T", "E'"], [], [], ["E", "T", "E'"], [], []],
            [[], ["E'", "+", "T", "E'"], [], [], ["E'"], ["E'", ]],
            [["T", "F", "T'"], [], [], ["T", "F", "T'"], [], []],
            [[], ["T'"], ["T'", "*", "F", "T'"],
             [], ["T'"], ["T'", ]],
            [["F", "x"], [], [], ["F", "(", "E", ")"], [], []],
        ]

        self.column_pos = {char: i for i, char in enumerate("x+*()$")}
        self.row_pos = {char: i for i, char in enumerate([
            "E", "E'", "T", "T'", "F"
        ])}

    def __getitem__(self, key):
        row, col = key
        row_pos = self.row_pos[row]
        column_pos = self.column_pos[col]
        return self.table[row_pos][column_pos]


class LL_1_Parser:
    def __init__(self, input_string) -> None:
        self.input_string = f"{input_string}$"
        self.table = SyntaxTable()
        self.cur_pos = 0

    def is_terminal(self, string):
        return string in "x+*()"

    def parse(self):
        char_stack = deque(["E", "$"])
        char_state = char_stack[0]

        char_stack_print = " ".join(list(char_stack))
        input_string_print = self.input_string[self.cur_pos:]
        action_type_print = ""
        print(f"{char_stack_print:20}{input_string_print:20}{action_type_print:10}")

        while char_state != "$":
            input_token = self.input_string[self.cur_pos]
            char_state = char_stack[0]

            if char_state == input_token:
                char_stack.popleft()
                action_type_print = f"Соответствие {input_token}"
                self.cur_pos += 1
            elif self.is_terminal(char_state):
                print("Syntax Error")
                break
            elif len(self.table[char_state, input_token]) == 0:
                print("Syntax Error")
                break
            elif len(self.table[char_state, input_token]) != 0:
                next_state = self.table[char_state, input_token]
                char_stack.popleft()

                next_state_list = list(next_state)
                left_rule = ''.join(next_state_list[1:])
                right_rule = next_state_list[0]

                if len(left_rule) == 0:
                    left_rule = "ε"
                action_type_print = f"{right_rule}->{left_rule}"

                left_rule = list(next_state)[1:]
                left_rule.reverse()
                char_stack.extendleft(left_rule)

            input_string_print = self.input_string[self.cur_pos:]
            char_stack_print = " ".join(list(char_stack))
            print(
                f"{char_stack_print:20}{input_string_print:20}{action_type_print:10}")


parser = LL_1_Parser("x+(x+x*x)")
parser.parse()
