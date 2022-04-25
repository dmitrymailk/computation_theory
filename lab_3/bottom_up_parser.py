from collections import deque

# https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/100%20Bottom-Up%20Parsing.pdf
# grammar rules in reverse order
Rule = {
    "E1": "E+T",
    "E0": "T",
    "T1": "T*f",
    "T0": "f",
    "f1": "(E)",
    "f0": "x",
}
Table = {
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

initial_string = "int+(int+int+int)"


class BottomUpParser:
    def __init__(self, expression):
        # @ is a end of string
        self.expression = f"{expression}@"

    def get_action_name(self, state, symbol):
        l = Table.get(symbol, None)
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
        l = Table.get(symbol, None)
        if l == None:
            return -1

        action = l[state]

        return int(action[1:])

    def get_replace(self, string):
        add = ""
        string = string[:]
        while len(string) != 0:
            for item in Rule.keys():
                if Rule[item] == string:
                    return add + item[0]

            add += string[0]
            string = string[1:]

        return "Replace not found"

    def format_state_stack(self, stk):
        result = ""
        states = stk[:]

        while len(states) != 0:
            result += str(states.pop(0)) + " "

        return result

    def LR(self, ):
        stateStack = []
        readyForm = ""

        # Подготовка к первому шагу
        stateStack.append(0)
        token = self.expression[0]

        print("{0,20}  |  {1, 20}  |", "State stack", "Result")

        while True:
            state = stateStack[-1]
            doing = self.get_action_name(state, token)

            tmp = self.format_state_stack(stateStack)

            tmp2 = readyForm + self.expression

            print("{0,20}  |  {1, 20}  |", tmp, tmp2)

            if doing == "end":
                break

            actNum = self.get_action_number(state, token)
            stateStack.pop()

            if doing == "shift":
                stateStack.append(actNum)
                readyForm += token
                self.expression = self.expression[1:]
                token = self.expression[0]
            elif doing == "reduce":
                readyForm = self.get_replace(readyForm)
                actNum = self.get_action_number(actNum, readyForm[-1])
                stateStack.append(actNum)


parser = BottomUpParser("x+x*x")
parser.LR()
