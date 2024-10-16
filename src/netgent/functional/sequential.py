from typing import List
from ..core.agent_wrapper import AgentWrapper

def sequential(agents: List[AgentWrapper], input: str) -> str:
    """
    Run agents sequentially and return the final output.

    This function implements the sequential processing workflow pattern
    as described in NetGent. It chains multiple agents for step-by-step
    processing, where each agent's output becomes the input for the next agent.

    Design:
    Initial ───► Agent1 ───► Agent2 ───► Agent3 ───► Final
    Input                                           Output

    Args:
        agents (List[AgentWrapper]): A list of AgentWrapper objects to be executed sequentially.
        input (str): The initial input to be passed to the first agent.
        callbacks (List[Callback], optional): List of callbacks to be executed. Defaults to None.

    Returns:
        str: The final output after all agents have been executed.

    Example:
        result = sequential([agent1, agent2, agent3], "What is the meaning of life?")
    """

    current_input: str = input
    for agent in agents:
        output = agent(current_input)
        current_input = output

    return current_input
