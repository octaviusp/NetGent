from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from ..core.agents import Agent
from ..core.states import State
from ..tools.base import Tool

class TextAgent(Agent, ABC):
    """
    Abstract base class for Text Model agents that process input state and return updated state.
    This class serves as a base for specific text model implementations.
    """
    def __init__(self, model_name: str, api_key: str, tools: Optional[List[Tool]] = None) -> None:
        """
        Initializes the TextAgent with a model name, API key, and optional tools.

        Args:
            model_name (str): The name of the text model to use.
            api_key (str): The API key for accessing the model.
            tools (Optional[List[Tool]]): List of tools available to the agent.
        """
        super().__init__(model_name, api_key, tools)
        self.model_name: str = model_name
        self.api_key: str = api_key
        self.model: Any = self._load_model()

    @abstractmethod
    def _load_model(self) -> Any:
        """
        Load the specified text model.

        Returns:
            Any: The loaded model object.
        """
        pass

    @abstractmethod
    def invoke(self, state: State) -> State:
        """
        Invokes the text model with the current state and updates it.

        Args:
            state (State): The current state containing input data.

        Returns:
            State: The updated state with the model's output.
        """
        pass

    @abstractmethod
    def process_with_text_model(self, input_data: Dict[str, Any]) -> str:
        """
        Processes the input data with the text model.

        Args:
            input_data (Dict[str, Any]): The input data to process.

        Returns:
            str: The result from the text model.
        """
        pass

class GPT3Agent(TextAgent):
    def _load_model(self) -> Any:
        # Implement GPT-3 model loading logic here
        pass

    def invoke(self, state: State) -> State:
        result = self.process_with_text_model(state.data)
        state.update({"text_result": result})
        return state

    def process_with_text_model(self, input_data: Dict[str, Any]) -> str:
        # Implement GPT-3 specific processing logic here
        return f"Processed by GPT-3: {self.model_name} with input: {input_data}"

class GPT4Agent(TextAgent):
    def _load_model(self) -> Any:
        # Implement GPT-4 model loading logic here
        pass

    def invoke(self, state: State) -> State:
        result = self.process_with_text_model(state.data)
        state.update({"text_result": result})
        return state

    def process_with_text_model(self, input_data: Dict[str, Any]) -> str:
        # Implement GPT-4 specific processing logic here
        return f"Processed by GPT-4: {self.model_name} with input: {input_data}"
