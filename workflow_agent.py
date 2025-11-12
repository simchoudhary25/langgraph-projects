#!/usr/bin/env python3
"""LangGraph workflow example using a prebuilt agent."""

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


# Define a simple tool
@tool
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    # This is a mock function - in a real scenario, you'd call a weather API
    return f"The weather in {city} is sunny and 72°F"


# Note: This example requires an LLM model. 
# For a complete example, you would need to provide a model like:
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(model="gpt-4")

if __name__ == "__main__":
    print("LangGraph Agent Workflow Example")
    print("=" * 50)
    print("\nThis example demonstrates how to create a LangGraph workflow with tools.")
    print("\nTo use this with a real LLM, you would:")
    print("1. Install langchain-openai or another LLM provider")
    print("2. Create a model: model = ChatOpenAI(model='gpt-4')")
    print("3. Create an agent: agent = create_react_agent(model, tools=[get_weather])")
    print("4. Run it: result = agent.invoke({'messages': [HumanMessage(content='What is the weather in SF?')]})")
    print("\nFor now, here's the tool definition:")
    print(f"Tool: {get_weather.name}")
    print(f"Description: {get_weather.description}")
    print(f"Example output: {get_weather.invoke({'city': 'San Francisco'})}")

