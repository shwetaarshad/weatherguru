import os
from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from tools.weather_tool import get_weather
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("LITELLM_API_KEY"),
    openai_api_base="https://lite-llm.mymaas.net",
    model_name="claude-3-5-sonnet",  # Update if you use a different model
    streaming=False,
    temperature=0.0,
)


weather_tool = Tool(
    name="WeatherInfo",
    func=get_weather,
    description="Get the current weather for a city. Input should be a city name like 'London'."
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def ask_weather_agent(prompt: str) -> str:
    return agent.run(prompt)
