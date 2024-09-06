from typing import List
from ..core.agent import Agent
from ..core.state import State

def sequential(agents: List[Agent], initial_state: State) -> State:
    """
    Run agents sequentially and return the final state.

    This function implements the sequential processing workflow pattern
    as described in NetGent. It chains multiple agents for step-by-step
    processing, where each agent's output becomes the input for the next agent.

    Design:
    Initial ───► Agent1 ───► Agent2 ───► Agent3 ───► Final
    State                                           State

    Args:
        agents (List[Agent]): A list of Agent objects to be executed sequentially.
        initial_state (State): The initial state to be passed to the first agent.

    Returns:
        State: The final state after all agents have been executed.

    Example:
        result = sequential([agent1, agent2, agent3], initial_state)
    """
    current_state: State = initial_state
    for agent in agents:
        current_state = agent.invoke(current_state)
    return current_state