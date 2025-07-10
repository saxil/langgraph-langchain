
# LangGraph

LangGraph is an extension of LangChain for building complex, stateful agentic applications. It allows you to represent your application as a graph, where nodes represent computations and edges represent the flow of control. This provides more control over the application's logic and enables the creation of multi-agent workflows.

## Key Concepts

### 1. Graph Representation

In LangGraph, you define your application as a graph. Each node in the graph is a function or a LangChain component, and the edges define the sequence of operations.

**Code Snippet:**

```python
from langgraph.graph import Graph

# Create a new graph
workflow = Graph()

# Add nodes to the graph
workflow.add_node("agent", agent)
workflow.add_node("tools", tool_executor)

# Set the entry and finish points of the graph
workflow.set_entry_point("agent")
workflow.set_finish_point("agent")

# Add edges to the graph
workflow.add_edge('agent', 'tools')
workflow.add_edge('tools', 'agent')

# Compile the graph into a runnable app
app = workflow.compile()
```

### 2. State Management

LangGraph introduces the concept of a state object that is passed between nodes in the graph. This allows you to maintain state throughout the execution of your application.

**Code Snippet:**

```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# Define the state object
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Use the state object in a node
def agent(state: State):
    # ...
    return {"messages": [ai_message]}
```

### 3. Conditional Edges

You can use conditional edges to control the flow of your application based on the current state.

**Code Snippet:**

```python
from langgraph.graph import END, START

# Define a conditional edge
def should_continue(state: State):
    if len(state["messages"]) > 6:
        return END
    return "tools"

# Add the conditional edge to the graph
workflow.add_conditional_edges(
    START,
    should_continue,
    {END: END, "tools": "tools"}
)
```

### 4. Multi-Agent Workflows

LangGraph is particularly well-suited for building multi-agent workflows, where different agents can collaborate to solve a problem.

**Code Snippet:**

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI

# Create a tool
def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor

# Create a node for the agent
def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=name)]}
```
