from netgent.core.agent_wrapper import AgentWrapper
from langchain_core.language_models.chat_models import BaseChatModel
from typing import Optional
from langgraph.graph.graph import CompiledGraph

def create_agent(
    chat_class: BaseChatModel | CompiledGraph,
    name: str = "agent",
    instructions: Optional[str] = None,
    **kwargs
) -> AgentWrapper:
    return AgentWrapper(
        name=name,
        chat_class=chat_class,
        instructions=instructions,
        **kwargs
    )
