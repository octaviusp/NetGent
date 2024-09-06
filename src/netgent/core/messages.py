from typing import Any, Dict, List, Optional, Union
from langchain_core.messages import BaseMessage

class NetGentMessage(BaseMessage):
    """
    Represents a message in the NetGent system.
    Inherits from langchain_core.messages.BaseMessage.
    """

    type: str = "netgent_message"

    def __init__(
        self,
        content: Union[str, List[Union[str, Dict]]],
        additional_kwargs: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        id: Optional[str] = None,
        response_metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize a NetGentMessage.

        Args:
            content (Union[str, List[Union[str, Dict]]]): The content of the message.
            additional_kwargs (Optional[Dict[str, Any]]): Additional keyword arguments.
            name (Optional[str]): An optional name for the message.
            id (Optional[str]): An optional unique identifier for the message.
            response_metadata (Optional[Dict[str, Any]]): Response metadata.
        """
        super().__init__(
            content=content,
            additional_kwargs=additional_kwargs,
            name=name,
            id=id,
            response_metadata=response_metadata,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the message to a dictionary representation."""
        return {
            "type": self.type,
            "content": self.content,
            "additional_kwargs": self.additional_kwargs,
            "name": self.name,
            "id": self.id,
            "response_metadata": self.response_metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NetGentMessage":
        """
        Create a NetGentMessage from a dictionary.

        Args:
            data (Dict[str, Any]): The dictionary containing message data.

        Returns:
            NetGentMessage: A new NetGentMessage instance.
        """
        return cls(
            content=data["content"],
            additional_kwargs=data.get("additional_kwargs", {}),
            name=data.get("name"),
            id=data.get("id"),
            response_metadata=data.get("response_metadata", {}),
        )

    def pretty_print(self) -> None:
        """Print a pretty representation of the message."""
        print(f"{self.type.capitalize()}: {self.content}")

    def pretty_repr(self, html: bool = False) -> str:
        """
        Get a pretty representation of the message.

        Args:
            html (bool): Whether to format the message as HTML.

        Returns:
            str: A pretty representation of the message.
        """
        if html:
            return f"<strong>{self.type.capitalize()}:</strong> {self.content}"
        return f"{self.type.capitalize()}: {self.content}"