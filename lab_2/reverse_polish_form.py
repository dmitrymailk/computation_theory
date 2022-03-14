infix_notation = "3+3*3-3"


def infix_to_postfix(infix_notation):
    """
    convertion fow single digits
    """
    stack = []
    RPM = []

    strength = {"+": 1, "-": 1, "*": 2, "/": 2}

    for char in infix_notation:
        if char.isdigit():
            RPM.append(int(char))
        elif char in ["-", "+", "*", "/"]:
            if len(stack) > 0:
                last_char = stack[-1]
                if strength[char] > strength[last_char]:
                    stack.append(char)
                else:
                    while len(stack) > 0 and strength[char] <= strength[last_char]:
                        last_char = stack.pop()
                        RPM.append(last_char)
                    stack.append(char)
            else:
                stack.append(char)

    for char in stack:
        RPM.append(char)

    return RPM

    print(RPM, stack)


infix_to_postfix(infix_notation=infix_notation)
