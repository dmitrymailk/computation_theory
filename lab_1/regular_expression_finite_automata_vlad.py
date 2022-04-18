from typing import List, Any, Callable
regular_expression_str = "(a|b|c)+(acd|adb)*"

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
        self.start_state: State = self.states[0]
        self.text: str = text + "\0"
        self.max_len: int = len(text)

    def start(self):
        # using Bread first search

        current_state: State = self.start_state
        prev_state: State = self.start_state
        i = 0
        text: str = self.text
        cur_len = 0
        last_final_state = 0
        last_final_state_len = 0
        sub_strings = []
        while i < len(text):
            char = text[i]
            print(f"{text[:i]}|{text[i:]}")
            is_next = False
            for arrow in current_state.out_transitions:
                arrow: TransitionArrow = arrow
                if arrow.condition(char):
                    prev_state = current_state
                    current_state = arrow.state
                    if current_state.state_type == STATE_TYPES["FINAL_STATE"]:
                        last_final_state = i + 1
                        last_final_state_len = cur_len + 1

                    cur_len += 1
                    is_next = True
                    i += 1
                    break

            if not is_next:
                if current_state.state_type == STATE_TYPES["FINAL_STATE"]:
                    if cur_len != 0:
                        sub_strings.append([i-cur_len, i])
                        print(text[i-cur_len: i])
                        last_final_state = 0
                        last_final_state_len = 0
                    i -= 1

                elif prev_state.state_type == STATE_TYPES["FINAL_STATE"]:
                    if cur_len != 0:
                        sub_strings.append([i-cur_len, i-1])
                        print(text[i-cur_len: i-1])
                        last_final_state = 0
                        last_final_state_len = 0
                    i -= 1

                # if prev_state.state_type == STATE_TYPES["FINAL_STATE"] and current_state.state_type == STATE_TYPES["FINAL_STATE"]:
                #     i -= 1

                if current_state.state_type != STATE_TYPES["CHAR_STATE"]:
                    i += 1

                if last_final_state != 0 and last_final_state_len != 0:
                    sub_strings.append([last_final_state -
                                        last_final_state_len, last_final_state])
                    print(text[last_final_state -
                          last_final_state_len: last_final_state])
                    last_final_state = 0
                    last_final_state_len = 0
                cur_len = 0
                prev_state = current_state
                current_state = self.start_state
                if char == '\0':
                    break

        return sub_strings

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
s_1 = State(state_type=final_state, name="s_1")
s_2 = State(state_type=char_state, name="s_2")
s_3 = State(state_type=char_state, name="s_3")
s_4 = State(state_type=char_state, name="s_4")
s_5 = State(state_type=final_state, name="s_5")
s_6 = State(state_type=final_state, name="s_6")

s_0_out_0 = TransitionArrow(state=s_1, condition=lambda c: c in "abc")
s_0.add_out_transition(s_0_out_0)

s_1_out_0 = TransitionArrow(state=s_1, condition=lambda c: c in 'abc')
s_1_out_1 = TransitionArrow(state=s_2, condition=lambda c: c == 'a')
s_1.add_out_transition(s_1_out_0)
s_1.add_out_transition(s_1_out_1)

s_2_out_0 = TransitionArrow(state=s_3, condition=lambda c: c == 'c')
s_2_out_1 = TransitionArrow(state=s_4, condition=lambda c: c == 'd')
s_2.add_out_transition(s_2_out_0)
s_2.add_out_transition(s_2_out_1)

s_3_out_0 = TransitionArrow(state=s_5, condition=lambda c: c == 'd')
s_3.add_out_transition(s_3_out_0)

s_4_out_0 = TransitionArrow(state=s_6, condition=lambda c: c == 'b')
s_4.add_out_transition(s_4_out_0)

s_5_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == 'a')
s_5.add_out_transition(s_5_out_0)

s_6_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == 'a')
s_6.add_out_transition(s_6_out_0)

states.append(s_0)
states.append(s_1)
states.append(s_2)
states.append(s_3)
states.append(s_4)
states.append(s_5)
states.append(s_6)

# text_1 = "abbabbbcabcab"
# text_1 = "aaaabbbaaabaaabbcabcabcabaaaabbbbabb"
# text_1 = "abcabcabab"
text_1 = "adbabdadbacddddadb"
# text_1 = "aaacabcabca"

fsm = StateMachine(states=states, text=text_1)


start_end_states = fsm.start()
print(start_end_states)


for item in start_end_states:
    start = item[0]
    end = item[1]

    print(
        f"{text_1[start:end]} - {text_1[:start]}\x1b[1;33m🢑{text_1[start:end]}\x1b[0m{text_1[end:]}")
