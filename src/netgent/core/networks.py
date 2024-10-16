from typing import List, Union, Dict
from netgent.core.agent_wrapper import AgentWrapper
from netgent.core.callbacks import BeforeInvokeCallback, AfterInvokeCallback, Callback
import concurrent.futures
from langchain_core.messages import BaseMessage
from netgent.core.state import AgentState

class NetworkAgent:
    """
    Parent class for creating networks of agents in NetGent.
    """

    def __init__(self, agents: List[AgentWrapper], callbacks: List[Callback] = None):
        """
        Initialize a NetworkAgent.

        Args:
            agents (List[AgentWrapper]): List of agents in the network.
            callbacks (List[Callback], optional): List of callbacks to be executed. Defaults to None.
        """
        self.agents: List[AgentWrapper] = agents
        self.callbacks: dict = {
            'before_invoke': None,
            'after_invoke': None
        }
        if callbacks:
            for callback in callbacks:
                if isinstance(callback, BeforeInvokeCallback):
                    self.callbacks['before_invoke'] = callback
                elif isinstance(callback, AfterInvokeCallback):
                    self.callbacks['after_invoke'] = callback

    def invoke(self, state: AgentState) -> AgentState:
        """
        Process the given input through the network of agents.

        Args:
            state (AgentState): Current state of the agent.

        Returns:
            AgentState: The updated state after processing through all agents.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def __call__(self, state: AgentState) -> AgentState:
        return self.invoke(state)

    def add_agent(self, agent: AgentWrapper) -> None:
        """
        Add an agent to the network.

        Args:
            agent (AgentWrapper): The agent to add to the network.
        """
        self.agents.append(agent)

    def remove_agent(self, agent: AgentWrapper) -> None:
        """
        Remove an agent from the network.

        Args:
            agent (AgentWrapper): The agent to remove from the network.
        """
        self.agents.remove(agent)

    def get_agents(self) -> List[AgentWrapper]:
        """
        Get the list of agents in the network.

        Returns:
            List[AgentWrapper]: The list of agents in the network.
        """
        return self.agents

class SequentialNetwork(NetworkAgent):
    """
    Sequential -> execute multiple agents one after another, where the output of one agent becomes the input for the next
    """
    def invoke(self, state: AgentState) -> AgentState:
        for agent in self.agents:
            if self.callbacks['before_invoke']:
                self.callbacks['before_invoke'](state)

            state = agent.invoke(state)

            if self.callbacks['after_invoke']:
                self.callbacks['after_invoke'](state)

        return state

class ParallelNetwork(NetworkAgent):
    """
    Parallel -> execute multiple agents at the same time and obtains its completions
    """
    def invoke(self, state: AgentState) -> AgentState:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            if self.callbacks['before_invoke']:
                self.callbacks['before_invoke'](state)

            futures = [executor.submit(agent.invoke, AgentState(messages=state['messages'].copy())) for agent in self.agents]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]

            # Merge results into a single AgentState
            merged_messages = state['messages'].copy()
            for result in results:
                # Only add the AI response, not the duplicated human message
                ai_response = result['messages'][-1]
                if isinstance(ai_response, BaseMessage):
                    merged_messages.append(ai_response)
                else:
                    merged_messages.append(("ai", ai_response))

            final_state = AgentState(messages=merged_messages)

            if self.callbacks['after_invoke']:
                self.callbacks['after_invoke'](final_state)

        return final_state
