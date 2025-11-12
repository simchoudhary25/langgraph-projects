#!/usr/bin/env python3
"""Run a LangGraph workflow example with streaming."""

from langgraph.graph import END, START, StateGraph, MessagesState
from langchain_core.messages import HumanMessage, AIMessage


def analyze_node(state: MessagesState) -> MessagesState:
    """Analyze the input message."""
    last_message = state["messages"][-1]
    analysis = f"Analyzing: '{last_message.content}' - This is a {len(last_message.content.split())} word message."
    return {"messages": state["messages"] + [AIMessage(content=analysis)]}


def generate_response_node(state: MessagesState) -> MessagesState:
    """Generate a response based on the analysis."""
    last_message = state["messages"][-1]
    response = f"Based on the analysis, here's the response: {last_message.content.replace('Analyzing: ', 'Response for ')}"
    return {"messages": state["messages"] + [AIMessage(content=response)]}


def main():
    """Run the workflow example."""
    # Create the workflow
    workflow = StateGraph(MessagesState)
    
    # Add nodes
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("generate", generate_response_node)
    
    # Add edges
    workflow.add_edge(START, "analyze")
    workflow.add_edge("analyze", "generate")
    workflow.add_edge("generate", END)
    
    # Compile the graph
    app = workflow.compile()
    
    # Run the workflow
    print("🚀 Running LangGraph Workflow")
    print("=" * 60)
    
    input_message = "What is LangGraph?"
    print(f"\n📥 Input: {input_message}")
    print("\n🔄 Executing workflow...\n")
    
    result = app.invoke({"messages": [HumanMessage(content=input_message)]})
    
    print("✅ Workflow execution complete!\n")
    print("📤 Output Messages:")
    print("-" * 60)
    for i, message in enumerate(result["messages"], 1):
        icon = "👤" if message.type == "human" else "🤖"
        print(f"{i}. {icon} {message.type.upper()}: {message.content}")
    
    # Demonstrate streaming
    print("\n" + "=" * 60)
    print("🌊 Streaming workflow execution...\n")
    
    stream_input = "Tell me about workflows"
    print(f"📥 Input: {stream_input}\n")
    
    print("📡 Streaming events:")
    print("-" * 60)
    for event in app.stream({"messages": [HumanMessage(content=stream_input)]}):
        for node_name, node_output in event.items():
            print(f"  → Node '{node_name}' completed")
            if "messages" in node_output:
                last_msg = node_output["messages"][-1]
                print(f"    └─ {last_msg.type.upper()}: {last_msg.content[:50]}...")
    
    print("\n✅ Streaming complete!")


if __name__ == "__main__":
    main()

