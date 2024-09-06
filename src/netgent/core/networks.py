from typing import List, Optional
from .agent import Agent
from .state import State

class NetworkAgent:
    """
    Parent class for creating networks of agents in NetGent.
    """

    def __init__(self, agents: List[Agent], initial_state: Optional[State] = None):
        """
        Initialize a NetworkAgent.

        Args:
            agents (List[Agent]): List of agents in the network.
            initial_state (Optional[State]): Initial state for the network. Defaults to None.
        """
        self.agents: List[Agent] = agents
        self.initial_state: Optional[State] = initial_state

    def invoke(self, state: Optional[State] = None) -> State:
        """
        Process the given state through the network of agents.

        Args:
            state (Optional[State]): Input state. If None, uses the initial_state.

        Returns:
            State: The final state after processing through all agents.

        Raises:
            ValueError: If no state is provided and initial_state is None.
        """
        current_state = state or self.initial_state
        if current_state is None:
            raise ValueError("No state provided and initial_state is None.")

        for agent in self.agents:
            current_state = agent.invoke(current_state)

        return current_state

    def add_agent(self, agent: Agent) -> None:
        """
        Add an agent to the network.

        Args:
            agent (Agent): The agent to add to the network.
        """
        self.agents.append(agent)

    def remove_agent(self, agent: Agent) -> None:
        """
        Remove an agent from the network.

        Args:
            agent (Agent): The agent to remove from the network.
        """
        self.agents.remove(agent)

    def get_agents(self) -> List[Agent]:
        """
        Get the list of agents in the network.

        Returns:
            List[Agent]: The list of agents in the network.
        """
        return self.agents