from abc import ABC, abstractmethod
from typing import List, Optional
from .state import State
from ..agents.llm import LLM
from ..tools.base import Tool

class Agent(LLM, ABC):
    """
    Base class for all agents in NetGent.
    Inherits from LLM and adds functionality for tools and prompts.
    """
    def __init__(self, model_name: str, api_key: str, tools: Optional[List[Tool]] = None):
        super().__init__(model_name, api_key)
        self.tools = tools or []
        self.prompt = None  # To be set by subclasses

    @abstractmethod
    def invoke(self, state: State) -> State:
        """
        Process the given state and return a new state.
        This method should be implemented by subclasses to define the agent's behavior.
        """
        pass

    def add_tool(self, tool: Tool):
        """
        Add a tool to the agent's toolkit.
        """
        self.tools.append(tool)

    def set_prompt(self, prompt: str):
        """
        Set the agent's prompt.
        """
        self.prompt = prompt

    def get_tools(self) -> List[Tool]:
        """
        Get the list of tools available to the agent.
        """
        return self.tools