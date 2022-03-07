from typing import List

regular_expression_str = "(ab+)*|(cab)+"

STATE_TYPES = {"FINAL_STATE": 256}


class State:
    def __init__(self, data: str) -> None:
        self.state_type: int = ord(data)


class TransitionArrow:
    def __init__(
        self,
        state: State,
    ) -> None:
        pass


class RegularExpressionParser:
    def __init__(self, regular_expression: str) -> None:
        self.regular_expression: str = regular_expression
        self.parsed_states: List[State] = []

    def __add_state(self, state: State) -> None:
        self.parsed_states.append(state)

    def parse(self) -> None:
        for char in self.regular_expression:
            print(char)
            if char.isalpha():
                state = State(char)
                self.__add_state(state)


# elif char == '+'


class StateMachine:
    def __init__(self, states: List[State]) -> None:
        self.states: List[State] = states
        self.current_state: State = self.states[0]

    def next_state(self, state: State) -> None:
        pass


print("program starts")

parser = RegularExpressionParser(regular_expression=regular_expression_str)

parser.parse()
