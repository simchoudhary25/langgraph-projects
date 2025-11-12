#!/usr/bin/env python3
"""Simple LangGraph workflow example."""

from typing import TypedDict

from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, StateGraph, MessagesState


def hello_node(state: MessagesState) -> MessagesState:
    """Simple node that adds a greeting message."""
    return {
        "messages": state["messages"] + [
            HumanMessage(content="Hello! This is a simple LangGraph workflow.")
        ]
    }


def goodbye_node(state: MessagesState) -> MessagesState:
    """Simple node that adds a farewell message."""
    return {
        "messages": state["messages"] + [
            HumanMessage(content="Goodbye! The workflow has completed.")
        ]
    }


# Create the workflow
workflow = StateGraph(MessagesState)

# Add nodes
workflow.add_node("hello", hello_node)
workflow.add_node("goodbye", goodbye_node)

# Add edges
workflow.add_edge(START, "hello")
workflow.add_edge("hello", "goodbye")
workflow.add_edge("goodbye", END)

# Compile the graph
app = workflow.compile()

# Run the workflow
if __name__ == "__main__":
    print("Running LangGraph workflow...")
    result = app.invoke({"messages": [HumanMessage(content="Start the workflow")]})
    
    print("\nWorkflow execution complete!")
    print("\nMessages:")
    for message in result["messages"]:
        print(f"  - {message.type}: {message.content}")

