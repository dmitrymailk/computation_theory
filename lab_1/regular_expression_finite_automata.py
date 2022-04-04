from typing import List, Any, Callable

regular_expression_str = "(ab+)*|(cab)+"

STATE_TYPES = {"FINAL_STATE": 0, "START_STATE": 1,
               "CHAR_STATE": 2, "ROOT_STATE": 3}

STATE_TYPES_STR = {STATE_TYPES[item]: item for item in STATE_TYPES.keys()}


class State:
    def __init__(self, state_type: int, name: str) -> None:
        self.state_type = state_type
        self.name = name
        self.out_transitions: List[Any] = []

    def add_out_transition(self, trans) -> None:
        self.out_transitions.append(trans)

    def __repr__(self) -> str:
        return self.name


class TransitionArrow:
    def __init__(self, state: State, condition: Callable) -> None:
        self.state: State = state
        self.condition: Callable = condition

    def __repr__(self) -> str:
        return self.state.name


# class RegularExpressionParser:
#     def __init__(self, regular_expression: str) -> None:
#         self.regular_expression: str = regular_expression
#         self.parsed_states: List[State] = []

#     def __add_state(self, state: State) -> None:
#         self.parsed_states.append(state)

#     def parse(self) -> None:
#         i = 0
#         prev_state = None
#         while i < len(self.regular_expression):
#             char = self.regular_expression[i]
#             if char.isalpha():
#                 code = STATE_TYPES["CHAR_STATE"]
#                 # state = State(code)


class StateMachine:
    def __init__(self, states: List[State], text: str) -> None:
        self.states: List[State] = states
        self.current_state: State = self.states[0]
        self.text: str = text + "\0"
        self.max_len: int = len(text)

    def start(self):
        # using Bread first search

        states = []
        states.append((self.states[0], []))
        text = self.text
        paths = []
        prev_states = []

        for i, char in enumerate(text):
            print(i, "-" * 50)

            state = states.pop(0)
            prev_states = state[1]
            print("prev_states before", prev_states)
            state: State = state[0]

            print(f"{state.name} : {STATE_TYPES_STR[state.state_type]}")
            current_char = f"{text[:i]}|{text[i:]}"
            print(current_char)
            print(char)

            counter = 0
            for tr in state.out_transitions:
                tr: TransitionArrow = tr
                if tr.condition(char):
                    counter += 1
                    state_type = tr.state.state_type

                    if state_type == STATE_TYPES["START_STATE"]:
                        states.append(
                            (
                                tr.state,
                                [(i, state_type, tr.state.name)],
                            )
                        )
                    elif state_type == STATE_TYPES["FINAL_STATE"]:
                        states.append(
                            (
                                tr.state,
                                [prev_states[0],
                                    (i, state_type, tr.state.name)],
                            )
                        )

                    else:
                        states.append(
                            (
                                tr.state,
                                [*prev_states],
                            )
                        )
            print("prev_states after", prev_states)

            if len(prev_states) > 1:
                paths.append(prev_states)

            if counter == 0:
                prev_states = []
                states.append((self.states[0], prev_states))

        if len(prev_states) > 1:
            paths.append(prev_states)
        print("last prev_states", prev_states)
        return paths

    def __str__(self) -> str:
        state_type = STATE_TYPES_STR[self.current_state.state_type]
        state_name = self.current_state.name
        return f"{state_name} : {state_type}"


print("program starts")

states = []
char_state = STATE_TYPES["CHAR_STATE"]
start_state = STATE_TYPES["START_STATE"]
final_state = STATE_TYPES["FINAL_STATE"]
root_state = STATE_TYPES["ROOT_STATE"]

s_0 = State(state_type=root_state, name="s_0")
s_1 = State(state_type=start_state, name="s_1")
s_2 = State(state_type=final_state, name="s_2")
s_3 = State(state_type=final_state, name="s_3")
s_4 = State(state_type=start_state, name="s_4")
s_5 = State(state_type=char_state, name="s_5")


s_0_out_0 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
s_0_out_1 = TransitionArrow(state=s_4, condition=lambda c: c == "c")
s_0.add_out_transition(s_0_out_0)
s_0.add_out_transition(s_0_out_1)

s_1_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == "b")
s_1_out_1 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
s_1.add_out_transition(s_1_out_0)
s_1.add_out_transition(s_1_out_1)

s_2_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == "b")
s_2_out_1 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
# s_2_out_2 = TransitionArrow(state=s_3, condition=lambda c: not c in ["a", 'b'])
s_2.add_out_transition(s_2_out_0)
s_2.add_out_transition(s_2_out_1)
# s_2.add_out_transition(s_2_out_2)

s_3_out_0 = TransitionArrow(state=s_4, condition=lambda c: c == "c")
# s_3_out_1 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
s_3.add_out_transition(s_3_out_0)
# s_3.add_out_transition(s_3_out_1)

s_4_out_0 = TransitionArrow(state=s_5, condition=lambda c: c == "a")
s_4.add_out_transition(s_4_out_0)

s_5_out_0 = TransitionArrow(state=s_3, condition=lambda c: c == "b")
s_5.add_out_transition(s_5_out_0)

states.append(s_0)
states.append(s_1)
states.append(s_2)
states.append(s_3)
states.append(s_4)
states.append(s_5)
# states.append(s_6)

# text_1 = "abbabbbcabcab"
text_1 = "aaaabbbaaabaaabbcabcabcabaaaabbbbabb"
# text_1 = "abcabcabab"

fsm = StateMachine(states=states, text=text_1)


start_end_states = fsm.start()
print(start_end_states)


for item in start_end_states:
    start = item[0][0]
    end = item[-1][0] + 1

    print(
        f"{text_1[start:end]} - {text_1[:start]}🢑{text_1[start:end]}🢑{text_1[end:]}")
