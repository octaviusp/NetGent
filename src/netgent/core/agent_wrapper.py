from typing import List, Optional, Dict, Union

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessage
from langgraph.graph.graph import CompiledGraph
from netgent.core.state import AgentState

class AgentWrapper():
    def __init__(
        self,
        chat_class: BaseChatModel | CompiledGraph,
        instructions: Optional[str] = None,
        name: str = "agent",
    ):
        """
        Initialize an EnhancedChat instance.

        Args:
            chat_class (type): The langchain chat class to use (e.g., ChatGroq).
            >> from langchain_groq import ChatGroq
            instructions (str, optional): Custom instructions or prompt for the model. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the chat class.
        """
        self.model = chat_class
        self.instructions = instructions
        self.name = name

    def invoke(self, state: AgentState) -> AgentState:
        if isinstance(self.model, CompiledGraph):
            return self._invoke_graph(state)
        else:
            return self._invoke_chat_model(state)

    def _invoke_graph(self, state: AgentState) -> AgentState:
        return self.model.invoke(state)

    def _invoke_chat_model(self, state: AgentState) -> AgentState:
        messages = state['messages']
        if self.instructions:
            messages = [SystemMessage(content=self.instructions)] + messages
        
        response = self.model.invoke(messages)
        return AgentState(messages=messages + [AIMessage(content=response.content)])

    async def ainvoke(self, state: AgentState) -> AgentState:
        if isinstance(self.model, CompiledGraph):
            return await self.model.ainvoke(state)
        else:
            messages = state['messages']
            if self.instructions:
                messages = [SystemMessage(content=self.instructions)] + messages
            
            response = await self.model.ainvoke(messages)
            return AgentState(messages=messages + [AIMessage(content=response.content)])
