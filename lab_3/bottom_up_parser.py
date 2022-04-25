from collections import deque

# https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/100%20Bottom-Up%20Parsing.pdf
# grammar rules in reverse order
grammar = {
    "E1": "E+T",
    "E0": "T",
    "T1": "T*f",
    "T0": "f",
    "f1": "(E)",
    "f0": "x",
}
table = {
    'E': ["s1", "", "", "", "", "", "", "", "s9", "", "", ""],
    'T': ["s4", "", "s3", "", "", "", "", "", "s4", "", "", ""],
    'f': ["s7", "", "s7", "", "", "s6", "", "", "s7", "", "", ""],
    '+': ["", "s2", "", "r0", "r1", "", "r2", "r3", "", "s2", "r4", "r5"],
    '*': ["", "", "", "s5", "s5", "", "r2", "r3", "", "", "r4", "r5"],
    '(': ["s8", "", "s8", "", "", "s8", "", "", "s8", "", "", ""],
    ')': ["", "s11", "", "r0", "r1", "", "r2", "r3", "", "s3", "r4", "r5"],
    'x': ["s11", "", "s11", "", "", "s11", "", "", "s11", "", "", ""],
    '@': ["", "end", "", "r0", "r1", "", "r2", "r3", "", "", "r4", "r5"],
}


class BottomUpParser:
    def __init__(self, expression):
        # @ is a end of string
        self.expression = f"{expression}@"

    def get_action_name(self, state, symbol):
        # принимаем решение что нам надо сделать свертку или сдвиг
        l = table.get(symbol, None)
        if l == None:
            return "Unknown symbol"

        action = l[state]

        if action == "end":
            return "end"

        if 's' in action:
            return 'shift'
        elif 'r' in action:
            return 'reduce'
        else:
            return "error"

    def get_action_number(self, state, symbol):
        l = table.get(symbol, None)
        if l == None:
            return -1

        action = l[state]

        return int(action[1:])

    def get_replace(self, string):
        add = ""
        # ищем подстроку пока она не совпадет с одной из продукций
        while len(string) != 0:
            for item in grammar.keys():
                if grammar[item] == string:
                    return add + item[0]

            add += string[0]
            string = string[1:]

        return "Replace not found"

    def format_state_stack(self, stack):
        result = ""
        states = stack[:]

        while len(states) != 0:
            result += str(states.pop(0)) + " "

        return result

    def LR(self, ):
        state_stack = []
        ready_form = ""

        # переходим в начальное состояние
        state_stack.append(0)
        token = self.expression[0]

        print("State stack\t", "Result")

        while True:
            state = state_stack[-1]
            action_type = self.get_action_name(state, token)

            state_number = self.format_state_stack(state_stack)

            temp_expression_form = ready_form + self.expression

            print(f"{state_number}\t\t", temp_expression_form)

            if action_type == "end":
                break

            act_num = self.get_action_number(state, token)
            state_stack.pop()

            if action_type == "shift":
                state_stack.append(act_num)
                ready_form += token
                self.expression = self.expression[1:]
                token = self.expression[0]

            elif action_type == "reduce":
                ready_form = self.get_replace(ready_form)
                act_num = self.get_action_number(act_num, ready_form[-1])
                state_stack.append(act_num)


parser = BottomUpParser("(x)+(x*x)*x")
parser.LR()
