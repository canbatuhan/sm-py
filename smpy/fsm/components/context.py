from state import State
from transition import Transition
from listener import Listener


class StateMachineContext:
    """
        Represents the context of a `FiniteStateMachine`. Stores information
        related to the current situation of the state machine and stores
        machine-specific variables (defined by the programmer).
    """

    def __init__(self) -> None:
        """
            Description:
                Creates a StateMachineContext object.
        """
        self.__current_state = None
        self.__last_event = None
        self.__last_transition = None
        self.__variables = dict()


    """
        Getters
    """
    def get_current_state(self) -> State:
        return self.__current_state

    def get_last_event(self) -> object:
        return self.__last_event

    def get_last_transition(self) -> Transition:
        return self.__last_transition

    def get_variables(self) -> dict: 
        return self.__variables


    """
        Setters
    """
    def set_current_state(self, state:State) -> None:
        self.__current_state = state

    def set_last_event(self, event:object) -> None:
        self.__last_event = event

    def set_last_transition(self, transition:Transition) -> None:
        self.__last_transition = transition

    def set_variables(self, variables:dict) -> None:
        self.__variables = variables
