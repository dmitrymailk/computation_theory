"""
Bottom up parser from dragon book for grammar
(1) E → E + T
(2) E → T
(3) T → T ∗ F
(4) T → F
(5) F → (E)
(6) F → x
"""


class Grammar:
    def __init__(self):
        self.rules = {
            1: ["E", "E+T"],
            2: ["E", "T"],
            3: ["T", "T*F"],
            4: ["T", "F"],
            5: ["F", "(E)"],
            6: ["F", "x"]
        }

    def __getitem__(self, key):
        return self.rules[key]


class Goto:
    def __init__(self):
        self.goto_column_pos = {
            "E": 0,
            "T": 1,
            "F": 2
        }

        self.goto_table = [
            [1, 2, 3],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [8, 2, 3],
            [-1, -1, -1],
            [-1, 9, 3],
            [-1, -1, 10],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
        ]

    def __getitem__(self, key):
        pos, char = key
        column_pos = self.goto_column_pos[char]
        return self.goto_table[pos][column_pos]


class Action:
    def __init__(self):
        self.action_table = [
            ["s5", "", "" "s4", "", ""],
            ["", "s6", "", "", "", "acc"],
            ["", "r2", "s7", "", "r2", "r2"],
            ["", "r4", "r4", "", "r4", "r4"],
            ["s5", "", "", "s4", "", ""],
            ["", "r6", "r6", "", "r6", "r6"],
            ["s5", "", "", "s4", "", ""],
            ["s5", "", "", "s4", "", ""],
            ["", "s6", "", "", "s11", ""],
            ["", "r1", "s7", "", "r1", "r1"],
            ["", "r3", "r3", "", "r3", "r3"],
            ["", "r5", "r5", "", "r5", "r5"]
        ]

        self.action_column_pos = {
            "x": 0,
            "+": 1,
            "*": 2,
            "(": 3,
            ")": 4,
            "$": 5
        }

    def __getitem__(self, key):
        char, pos = key
        column_pos = self.action_column_pos[char]
        return self.action_table[pos][column_pos]


class LR_Parser:
    def __init__(self, input_string):
        self.action = Action()
        self.goto = Goto()
        self.grammar = Grammar()

        self.input_string = f"{input_string}$"
        self.cur_pos = 0

    def parse(self):
        char_stack = []
        state_stack = [0]
        input_char = self.input_string[self.cur_pos]
        state = state_stack[-1]
        while True:

            state = state_stack[-1]
            action_type = self.action[input_char, state]
            # print(f"Вход: {}")
            # print(char_stack)
            input_string_print = self.input_string[self.cur_pos:]
            state_stack_print = state_stack
            if action_type == "acc":
                print("Accepted")
                break

            if 's' in action_type:
                # print(f"Shift {action_type}")
                state = int(action_type[1:])
                state_stack.append(state)
                self.cur_pos += 1
                char_stack.append(input_char)
                print(char_stack)
                input_char = self.input_string[self.cur_pos]

            elif 'r' in action_type:
                # print(char_stack)
                production_num = int(action_type[1:])
                rule = self.grammar[production_num]
                b_rule_len = len(rule[1])
                char_stack = char_stack[:-b_rule_len]
                state_stack = state_stack[:-b_rule_len]
                char_stack.append(rule[0])

                state = state_stack[-1]
                goto_state = self.goto[state, rule[0]]
                state_stack.append(goto_state)
                print(char_stack)
                # print("->".join(rule))
                # print(f"str = {''.join(char_stack)}{self.input_string[self.cur_pos:]}")
            else:
                print("Error")
                break
            # print(char_stack)
            # print("----")


parser = LR_Parser("x*x+x")
parser.parse()
