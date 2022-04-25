def postfix_to_infix(expression):

    stack = []
    i = 0
    while i < len(expression):
        char = expression[i]

        if expression[i:i+4] == "sqrt":
            operator_1 = stack.pop(0)
            operator_2 = stack.pop(0)
            stack.insert(0, f"sqrt({operator_1})")
            i += 4

        elif char.isdigit():
            stack.insert(0, char)
            i += 1
        else:
            operator_1 = stack.pop(0)
            operator_2 = stack.pop(0)
            stack.insert(0, "(" + operator_2 + char +
                         operator_1 + ")")
            i += 1

    return stack[0]


exp = "02232*+*2*-"
exp = "0003-22*+sqrt7*-1154*+*356*+2+*0145*+1+sqrt*+"
# sqrt(-3+2*2)*7+1*(1+5*4)*(3+5*6+2)*sqrt(1+4*5+1)
exp = "003-22*+sqrt7*1154*+*356*+2+*0145*+1+sqrt*+"
# 3+sqrt(5)*6/6+sqrt(7)
exp = "305sqrt6*6/+07sqrt+"
print(postfix_to_infix(exp))
