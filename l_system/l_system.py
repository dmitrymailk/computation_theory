from turtle import Turtle

t = Turtle()
t.color("deeppink", "yellow")
t.speed(0)
# t.tracer(False)

###

axiom = "F-F-F-F"
# axiom = "F--F--F"

amount_iterations = 1

RULES = {
    "F": "FF-F-F-F-FF"
    # "F": "F+F--F+F"
}

for i in range(amount_iterations):
    new_axiom = ""
    for char in axiom:
        if char in RULES:
            new_axiom += RULES[char]
        else:
            new_axiom += char
    axiom = new_axiom
###

angle = 90
# angle = 60
step = 10

for char in axiom:
    stack = []
    if char == "F":
        t.forward(step)
    elif char == '-':
        t.left(angle=angle)
    elif char == '+':
        t.right(angle=angle)
    elif char == "[":
        stack.append((t.position(), t.heading()))
    elif char == ']':
        t.pu()
        p, h = stack.pop()
        t.goto(p)
        t.setheading(h)

print(axiom)
t.screen.mainloop()
