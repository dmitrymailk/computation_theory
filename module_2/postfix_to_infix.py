def postfix_to_infix(expression):

    stack = []

    for char in expression:

        # Push operands
        if char.isdigit() or char.isalpha():
            stack.insert(0, char)
        else:
            operator_1 = stack.pop(0)
            operator_2 = stack.pop(0)
            stack.insert(0, "(" + operator_2 + char +
                         operator_1 + ")")

    return stack[0]


exp = "02232*+*2*-"
print(postfix_to_infix(exp))
