infix_notation = "3+3*3-3"
infix_notation_1 = "(4+7)+2/3"


def infix_to_postfix_1(infix_notation):
    """
    convertion fow single digits
    without parentheses
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


def infix_to_postfix_2(infix_notation):
    """
    convertion fow single digits
    with parentheses
    """
    stack = []
    RPM = []

    strength = {"+": 1, "-": 1, "*": 2, "/": 2}

    for char in infix_notation:
        if char.isdigit():
            RPM.append(int(char))
        elif char in ["-", "+", "*", "/", "(", ")"]:
            if len(stack) > 0:
                if not char in ["(", ")"]:
                    last_char = stack[-1]
                    if not last_char in ["(", ")"]:
                        if strength[char] > strength[last_char]:
                            stack.append(char)
                        else:
                            while (
                                len(stack) > 0 and strength[char] <= strength[last_char]
                            ):
                                last_char = stack.pop()
                                RPM.append(last_char)
                            stack.append(char)
                    else:
                        stack.append(char)
                else:
                    if char == "(":
                        stack.append(char)
                    else:
                        last_char = stack.pop()
                        while len(stack) > 0 and last_char != "(":
                            RPM.append(last_char)
                            last_char = stack.pop()
            else:
                stack.append(char)

    # simply getting operations from stack and passing them to RPM
    for char in stack[::-1]:
        RPM.append(char)

    print(RPM)
    return RPM


infix_to_postfix_1(infix_notation=infix_notation)
infix_to_postfix_2(infix_notation=infix_notation_1)