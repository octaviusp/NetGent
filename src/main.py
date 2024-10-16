from langchain_openai import ChatOpenAI
from netgent.core.callbacks import AfterInvokeCallback, BeforeInvokeCallback
from netgent.core.networks import ParallelNetwork, SequentialNetwork
from netgent.functional.agents import create_agent
from netgent.functional.sequential import sequential
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from netgent.core.state import AgentState

load_dotenv()

# Initialize the ChatOpenAI model
gpt_4 = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.0
)

# Initialize the ChatOpenAI model
llama_3_8b = ChatGroq(
    model_name="llama3-8b-8192",
    temperature=0.0
)


@tool("Search")
def weather(city: str) -> str:
    """
    Get the weather for a city
    """
    return f"The weather in {city} is 20 degrees"

gpt_4_w_tools = create_react_agent(model=gpt_4, tools=[weather])

english_agent = create_agent(
    chat_class=gpt_4,
    instructions="Answer in English.",
    name="weather_agent"
)

spanish_agent = create_agent(
    chat_class=gpt_4,
    instructions="Answer in Spanish.",
    name="weather_agent"
)

parallel_layer = ParallelNetwork(
    agents=[english_agent, spanish_agent],
    callbacks=[BeforeInvokeCallback(), AfterInvokeCallback()]
)

initial_state = AgentState(messages=[("human", "Hola!")])

result_state = parallel_layer(initial_state)

print(result_state)
# Uncomment and modify as needed for additional examples
# philosopher = create_agent(
#     chat_class=llama_3_8b,
#     instructions="You are Socrates, you are a philosopher and you are talking with a user.",
#     name="philosopher"
# )
# 
# translater = create_agent(
#     chat_class=llama_3_8b,
#     instructions="Translate the response into Spanish without losing information and adding anything.",
#     name="translater"
# )
# 
# offensive_guard = create_agent(
#     chat_class=llama_3_8b,
#     instructions="Answer if this is an offensive response or not. Simple response, just yes or no.",
#     name="offensive_guard"
# )
# 
# sequential_layer = SequentialNetwork(
#     agents=[philosopher, translater, offensive_guard],
#     callbacks=[BeforeInvokeCallback(), AfterInvokeCallback()]
# )
# 
# initial_state = AgentState(messages=[("human", "What is the meaning of life?")])
# result_state = sequential_layer.invoke(initial_state)
# print(result_state)
