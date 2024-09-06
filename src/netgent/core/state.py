from typing import Any, Dict, Optional
from langchain_core.stores import BaseStore

class State(BaseStore):
    """
    Represents the state of an agent or workflow in NetGent.
    Implements the BaseStore interface for compatibility with LangChain.
    """
    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self.data: Dict[str, Any] = data or {}

    def set(self, key: str, value: Any) -> None:
        """Set a key-value pair in the state."""
        self.data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the state."""
        return self.data.get(key, default)

    def delete(self, key: str) -> None:
        """Delete a key-value pair from the state."""
        self.data.pop(key, None)

    def exists(self, key: str) -> bool:
        """Check if a key exists in the state."""
        return key in self.data

    def clear(self) -> None:
        """Clear all key-value pairs from the state."""
        self.data.clear()

    def update(self, new_data: Dict[str, Any]) -> None:
        """Update the state with new data."""
        self.data.update(new_data)