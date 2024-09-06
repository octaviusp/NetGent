from abc import ABC, abstractmethod
from ..core.agent import Agent
from ..core.state import State
from typing import Any, Dict

class LLM(Agent, ABC):
    """
    Abstract base class for Language Model agents that process input state and return updated state.
    This class serves as a base for specific language model implementations.
    """
    def __init__(self, model_name: str, api_key: str) -> None:
        """
        Initializes the LLM agent with a model name and API key.

        Args:
            model_name (str): The name of the language model to use.
            api_key (str): The API key for accessing the model.
        """
        self.model_name = model_name
        self.api_key = api_key

    @abstractmethod
    def invoke(self, state: State) -> State:
        """
        Invokes the language model with the current state and updates it.

        Args:
            state (State): The current state containing input data.

        Returns:
            State: The updated state with the model's output.
        """
        pass

    @abstractmethod
    def process_with_llm(self, input_data: Dict[str, Any]) -> str:
        """
        Processes the input data with the language model.

        Args:
            input_data (Dict[str, Any]): The input data to process.

        Returns:
            str: The result from the language model.
        """
        pass

class GPT3Agent(LLM):
    def invoke(self, state: State) -> State:
        result = self.process_with_llm(state.data)
        state.update({"llm_result": result})
        return state

    def process_with_llm(self, input_data: Dict[str, Any]) -> str:
        # Implement GPT-3 specific processing logic here
        return f"Processed by GPT-3: {self.model_name} with input: {input_data}"

class GPT4Agent(LLM):
    def invoke(self, state: State) -> State:
        result = self.process_with_llm(state.data)
        state.update({"llm_result": result})
        return state

    def process_with_llm(self, input_data: Dict[str, Any]) -> str:
        # Implement GPT-4 specific processing logic here
        return f"Processed by GPT-4: {self.model_name} with input: {input_data}"
