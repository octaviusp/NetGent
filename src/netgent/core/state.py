from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage

def add_messages(existing: Sequence[BaseMessage], new: Sequence[BaseMessage]) -> Sequence[BaseMessage]:
    """Aggregate function to append new messages to existing messages."""
    return list(existing) + list(new)

class AgentState(TypedDict):
    """The state of the agent."""

    messages: Annotated[Sequence[BaseMessage], add_messages]

