import os
from pathlib import Path

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def create_project_structure():
    # Create main directories
    create_directory('src')
    create_directory('src/agents')
    create_directory('src/tools')
    create_directory('src/networks')
    create_directory('src/callbacks')

    # Create main.py
    main_content = '''
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from netgent.core.state import AgentState
from agents.english_agent import english_agent
from agents.spanish_agent import spanish_agent
from networks.parallel_network import parallel_layer
from tools.weather_tool import weather

load_dotenv()

def main():
    initial_state = AgentState(messages=[("human", "Hola!")])
    result_state = parallel_layer(initial_state)
    print(result_state)

if __name__ == "__main__":
    main()
'''
    create_file('src/main.py', main_content.strip())

    # Create agents
    english_agent_content = '''
from langchain_openai import ChatOpenAI
from netgent.functional.agents import create_agent

gpt_4 = ChatOpenAI(model_name="gpt-4", temperature=0.0)

english_agent = create_agent(
    chat_class=gpt_4,
    instructions="Answer in English.",
    name="english_agent"
)
'''
    create_file('src/agents/english_agent.py', english_agent_content.strip())

    spanish_agent_content = '''
from langchain_openai import ChatOpenAI
from netgent.functional.agents import create_agent

gpt_4 = ChatOpenAI(model_name="gpt-4", temperature=0.0)

spanish_agent = create_agent(
    chat_class=gpt_4,
    instructions="Answer in Spanish.",
    name="spanish_agent"
)
'''
    create_file('src/agents/spanish_agent.py', spanish_agent_content.strip())

    # Create tools
    weather_tool_content = '''
from langchain_core.tools import tool

@tool("Search")
def weather(city: str) -> str:
    """
    Get the weather for a city
    """
    return f"The weather in {city} is 20 degrees"
'''
    create_file('src/tools/weather_tool.py', weather_tool_content.strip())

    # Create networks
    parallel_network_content = '''
from netgent.core.networks import ParallelNetwork
from netgent.core.callbacks import AfterInvokeCallback, BeforeInvokeCallback
from agents.english_agent import english_agent
from agents.spanish_agent import spanish_agent

parallel_layer = ParallelNetwork(
    agents=[english_agent, spanish_agent],
    callbacks=[BeforeInvokeCallback(), AfterInvokeCallback()]
)
'''
    create_file('src/networks/parallel_network.py', parallel_network_content.strip())

    # Create callbacks (empty files for now)
    create_file('src/callbacks/__init__.py', '')

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
