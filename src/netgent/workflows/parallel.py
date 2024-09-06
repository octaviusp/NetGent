from typing import List, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..core.agent import Agent
from ..core.state import State

def parallel(agents: List[Agent], initial_state: State, aggregated: bool = False) -> Union[List[State], State]:
    """
    Run agents in parallel and return a list of resulting states or an aggregated state.

    This function implements the parallel processing workflow pattern
    as described in NetGent. It executes multiple agents concurrently,
    where each agent processes the initial state independently.

    Design:
                 ┌─────► Agent1 ─────┐
                 │                   │
    Initial ─────┼─────► Agent2 ─────┼───► Results
    State        │                   │
                 └─────► Agent3 ─────┘

    Args:
        agents (List[Agent]): A list of Agent objects to be executed in parallel.
        initial_state (State): The initial state to be passed to all agents.
        aggregated (bool): If True, concatenate all final states into a single state. Default is False.

    Returns:
        Union[List[State], State]: A list of final states (if aggregated is False) or a single aggregated state (if aggregated is True).

    Example:
        results = parallel([agent1, agent2, agent3], initial_state)
        aggregated_result = parallel([agent1, agent2, agent3], initial_state, aggregated=True)

    Note:
        This function evaluates all agents simultaneously and waits for all
        executions to finish before returning the results.
    """
    def invoke_agent(agent: Agent) -> State:
        return agent.invoke(initial_state)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(invoke_agent, agent) for agent in agents]
        results = [future.result() for future in as_completed(futures)]

    if aggregated:
        final_state = State({})
        for result in results:
            final_state.update(result.data)
        return final_state
    else:
        return results