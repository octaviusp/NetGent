from netgent.core.agent_wrapper import AgentWrapper
from netgent.core.state import AgentState
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio

def parallel(agents: List[AgentWrapper], state: AgentState) -> List[AgentState]:
    """
    Run agents in parallel and return a list of resulting AgentStates.

    This function implements the parallel processing workflow pattern
    as described in NetGent. It executes multiple agents concurrently,
    where each agent processes the input state independently.

    Design:
                 ┌─────► Agent1 ─────┐
                 │                   │
    Input   ─────┼─────► Agent2 ─────┼───► Results
    State        │                   │     States
                 └─────► Agent3 ─────┘

    Args:
        agents (List[AgentWrapper]): A list of AgentWrapper objects to be executed in parallel.
        state (AgentState): The input state to be passed to all agents.

    Returns:
        List[AgentState]: A list of output states from all agents.

    Example:
        results = parallel([agent1, agent2, agent3], initial_state)
    """

    def invoke_agent(agent: AgentWrapper) -> AgentState:
        return agent.invoke(state.copy())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(invoke_agent, agent) for agent in agents]
        results = [future.result() for future in as_completed(futures)]

    return results

async def aparallel(agents: List[AgentWrapper], state: AgentState) -> List[AgentState]:
    """
    Run agents in parallel asynchronously and return a list of resulting AgentStates.

    This function implements the asynchronous parallel processing workflow pattern
    as described in NetGent. It executes multiple agents concurrently and asynchronously,
    where each agent processes the input state independently.

    Design:
                 ┌─────► Agent1 ─────┐
                 │                   │
    Input   ─────┼─────► Agent2 ─────┼───► Results
    State        │                   │     States
                 └─────► Agent3 ─────┘

    Args:
        agents (List[AgentWrapper]): A list of AgentWrapper objects to be executed in parallel.
        state (AgentState): The input state to be passed to all agents.

    Returns:
        List[AgentState]: A list of output states from all agents.

    Example:
        results = await aparallel([agent1, agent2, agent3], initial_state)
    """

    async def ainvoke_agent(agent: AgentWrapper) -> AgentState:
        return await agent.ainvoke(state.copy())

    tasks = [ainvoke_agent(agent) for agent in agents]
    results = await asyncio.gather(*tasks)

    return results
