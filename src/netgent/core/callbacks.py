from abc import ABC, abstractmethod

class Callback(ABC):
    @staticmethod
    @abstractmethod
    def __call__(data) -> None:
        """
        Abstract method to be implemented by all callback classes.
        
        Args:
            data (str): The data to be processed by the callback.
        """
        pass

    @staticmethod
    def __name__():
        return Callback.__name__.lower()

class BeforeInvokeCallback(Callback):
    
    @staticmethod
    def __call__(data) -> None:
        """
        Callback method to be called before invoking an agent.
        
        Args:
            data (str): The input data before agent invocation.
        """
        print(f"Before invoke: {data}")

    @staticmethod
    def __repr__():
        return "before_invoke_callback"

class AfterInvokeCallback(Callback):
    
    @staticmethod
    def __call__(data) -> None:
        """
        Callback method to be called after invoking an agent.
        
        Args:
            data (str): The output data after agent invocation.
        """
        print(f"After invoke: {data}")

    @staticmethod
    def __repr__():
        return "after_invoke_callback"
