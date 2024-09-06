from typing import List, Optional, Callable
from ..state import State
from ..agent import Agent

def chain_of_thought_prompt(agent: Agent, state: State) -> State:
    """
    Implement a chain of thought prompt for step-by-step thinking.

    Args:
        agent (Agent): The agent to use for processing.
        state (State): The initial state.

    Returns:
        State: The final state after chain of thought processing.
    """
    prompt = """
    Let's approach this step-by-step:
    1. Analyze the given information
    2. Break down the problem into smaller parts
    3. Consider each part individually
    4. Synthesize the findings
    5. Draw a conclusion

    For each step, explain your thought process clearly.

    Given information:
    {state}

    Now, let's begin the step-by-step analysis:
    """

    updated_state = state.copy()
    updated_state.update({"prompt": prompt.format(state=state.data)})
    return agent.invoke(updated_state)

def average_result_prompt(
    agent: Agent,
    state: State,
    k: int = 3,
    evaluator_agent: Optional[Agent] = None
) -> State:
    """
    Invoke an agent K times, concatenate responses, and extract the best answer.

    Args:
        agent (Agent): The agent to use for processing.
        state (State): The initial state.
        k (int): Number of times to invoke the agent. Default is 3.
        evaluator_agent (Optional[Agent]): An optional agent to evaluate the final result.

    Returns:
        State: The final state with the best answer.
    """
    results: List[State] = []
    
    for _ in range(k):
        results.append(agent.invoke(state))
    
    concatenated_results = "\n\n".join([str(result.data) for result in results])
    
    prompt = f"""
    You have been given {k} different responses to the same query. Your task is to:
    1. Analyze each response
    2. Identify the key points and insights from each
    3. Synthesize the best elements into a single, comprehensive answer
    4. Ensure the final answer is coherent, accurate, and addresses the original query

    Here are the responses:

    {concatenated_results}

    Please provide the best possible answer based on these responses:
    """

    updated_state = state.copy()
    updated_state.update({"prompt": prompt})
    best_answer = agent.invoke(updated_state)

    if evaluator_agent:
        evaluation_prompt = f"""
        Please evaluate the following answer for accuracy, completeness, and relevance:

        {best_answer.data}

        Provide your evaluation and any suggestions for improvement:
        """
        evaluation_state = state.copy()
        evaluation_state.update({"prompt": evaluation_prompt})
        evaluation = evaluator_agent.invoke(evaluation_state)
        
        best_answer.update({"evaluation": evaluation.data})

    return best_answer