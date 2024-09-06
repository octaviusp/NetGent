from netgent.core.state import State
from netgent.agents.llm import LLM
from netgent.workflows.sequential import sequential

def main() -> None:
    """
    Main entry point of the application.
    """
    initial_state = State({"input": "Hello, NetGent!"})
    
    llm1 = LLM("gpt-3.5-turbo")
    llm2 = LLM("gpt-4")
    
    final_state = sequential([llm1, llm2], initial_state)
    
    print(f"Final state: {final_state.data}")

if __name__ == "__main__":
    main()