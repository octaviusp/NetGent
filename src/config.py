from typing import Dict, Any

class Config:
    """
    Configuration class for the application.
    """
    DEBUG: bool = False
    API_KEY: str = "your_api_key_here"

    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """
        Returns the configuration as a dictionary.
        """
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('__')}