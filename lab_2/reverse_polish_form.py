infix_notation = "3+3*3-3"
infix_notation_1 = "(4+7)+2/3"
infix_notation_2 = "1+2*(3-4)"


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
            RPM.append(char)
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
                                if stack[-1] == "(":
                                    break
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

    # print(RPM)
    return "".join(RPM)


def infix_to_postfix_3(infix_notation):
    """
    convertion for multiple digits
    with parentheses
    """
    stack = []
    RPM = []

    strength = {"+": 1, "-": 1, "*": 2, "/": 2}
    i = 0
    while i < len(infix_notation):
        char = infix_notation[i]
        if char.isdigit():
            num = f"{char}"
            old_pos = int(i)
            if i < len(infix_notation) - 1:
                while (
                    infix_notation[i + 1].isdigit() or infix_notation[i + 1] == "."
                ) and i < len(infix_notation):
                    num += infix_notation[i + 1]
                    i += 1
            # if old_pos == i:
            i += 1
            num += ";"
            RPM.append(num)

        elif char in ["-", "+", "*", "/", "(", ")"]:
            if len(stack) > 0:
                if not char in ["(", ")"]:
                    last_char = stack[-1]
                    if not last_char in ["(", ")"]:
                        if strength[char] > strength[last_char]:
                            stack.append(char)
                            i += 1
                        else:
                            while (
                                len(stack) > 0 and strength[char] <= strength[last_char]
                            ):
                                if stack[-1] == "(":
                                    break
                                last_char = stack.pop()
                                RPM.append(last_char)

                            stack.append(char)
                            i += 1
                    else:
                        stack.append(char)
                        i += 1
                else:
                    if char == "(":
                        stack.append(char)
                        i += 1
                    else:
                        last_char = stack.pop()
                        while len(stack) > 0 and last_char != "(":
                            RPM.append(last_char)
                            last_char = stack.pop()
                        i += 1
            else:
                stack.append(char)
                i += 1

    # simply getting operations from stack and passing them to RPM
    for char in stack[::-1]:
        RPM.append(char)

    # print(RPM)
    return "".join(RPM)


# infix_to_postfix_1(infix_notation=infix_notation)
# infix_to_postfix_2(infix_notation=infix_notation_1)
# infix_to_postfix_2(infix_notation=infix_notation_2)
examples = [["(6.6+9-5.2)/(0.8+1*2)+7", "6.6;9;+5.2;-0.8;1;2;*+/7;+"]]

for item in examples:
    infix_str = item[0].replace("-", "")
    # -6 = 6 * -1
    predict = infix_to_postfix_3(item[0])
    # if predict != item[1]:
    print(f"{item[1]}\n{predict}")
