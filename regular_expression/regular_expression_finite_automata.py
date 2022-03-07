from turtle import st
from typing import List, Any, Callable
from unicodedata import name

regular_expression_str = "(ab+)*|(cab)+"

STATE_TYPES = {"FINAL_STATE": 0, "START_STATE": 1, "CHAR_STATE": 2}
STATE_TYPES_STR = {STATE_TYPES[item]: item for item in STATE_TYPES.keys()}


class State:
    def __init__(self, state_type: int, name: str) -> None:
        self.state_type = state_type
        self.name = name
        self.out_transitions: List[Any] = []

    def add_out_transition(self, trans) -> None:
        self.out_transitions.append(trans)


class TransitionArrow:
    def __init__(self, state: State, condition: Callable) -> None:
        self.state: State = state
        self.condition: Callable = condition


class RegularExpressionParser:
    def __init__(self, regular_expression: str) -> None:
        self.regular_expression: str = regular_expression
        self.parsed_states: List[State] = []

    def __add_state(self, state: State) -> None:
        self.parsed_states.append(state)

    def parse(self) -> None:
        i = 0
        prev_state = None
        while i < len(self.regular_expression):
            char = self.regular_expression[i]
            if char.isalpha():
                code = STATE_TYPES["CHAR_STATE"]
                # state = State(code)


class StateMachine:
    def __init__(self, states: List[State], text: str) -> None:
        self.states: List[State] = states
        self.current_state: State = self.states[0]
        self.text: str = text
        self.max_len: int = len(text)

    def start(self):
        # using Bread first search

        states: List[State] = []
        states.append(self.states[0])
        text = self.text

        for i, char in enumerate(text):
            print("-" * 100)

            state: State = states.pop(0)
            print(f"{state.name} : {STATE_TYPES_STR[state.state_type]}")
            print(f"{text[:i]}|{text[i:]}")
            print(char)

            for tr in state.out_transitions:
                tr: TransitionArrow = tr
                if tr.condition(char):
                    states.append(tr.state)

    def __str__(self) -> str:
        state_type = STATE_TYPES_STR[self.current_state.state_type]
        state_name = self.current_state.name
        return f"Current state {state_name} : {state_type}"


print("program starts")

states = []
char_state = STATE_TYPES["CHAR_STATE"]
start_state = STATE_TYPES["START_STATE"]
final_state = STATE_TYPES["FINAL_STATE"]

s_0 = State(state_type=start_state, name="s_0")
states.append(s_0)

s_1 = State(state_type=char_state, name="s_1")
s_2 = State(state_type=final_state, name="s_2")
s_3 = State(state_type=final_state, name="s_3")
s_4 = State(state_type=char_state, name="s_4")
s_5 = State(state_type=char_state, name="s_5")


s_0_out_0 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
s_0_out_1 = TransitionArrow(state=s_4, condition=lambda c: c == "c")
s_0.add_out_transition(s_0_out_0)
s_0.add_out_transition(s_0_out_1)

s_1_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == "b")
s_1.add_out_transition(s_1_out_0)

s_2_out_0 = TransitionArrow(state=s_2, condition=lambda c: c == "b")
s_2_out_1 = TransitionArrow(state=s_1, condition=lambda c: c == "a")
s_2_out_2 = TransitionArrow(state=s_4, condition=lambda c: c == "c")
s_2.add_out_transition(s_2_out_0)
s_2.add_out_transition(s_2_out_1)
s_2.add_out_transition(s_2_out_2)

s_3_out_0 = TransitionArrow(state=s_4, condition=lambda c: c == "c")
s_3.add_out_transition(s_3_out_0)

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

text = "abbabbbcabcab"

fsm = StateMachine(states=states, text=text)

fsm.start()
