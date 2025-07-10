
# LangSmith

LangSmith is a platform for debugging, testing, evaluating, and monitoring LLM applications. It provides visibility into how your application is performing and helps you to improve it over time.

## Key Features

### 1. Tracing

LangSmith automatically traces the execution of your LangChain components, providing a detailed view of how your application is working.

**Code Snippet:**

```python
import os
from langsmith import Client

# Set up LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "YOUR_API_KEY"

client = Client()

# Your LangChain code here
```

### 2. Debugging

LangSmith makes it easy to debug your applications by providing detailed information about each step in the execution trace.

### 3. Testing and Evaluation

LangSmith allows you to create datasets and run evaluations to test the performance of your applications.

**Code Snippet:**

```python
from langsmith.evaluation import evaluate

# Define your model
def my_model(inputs):
    # ...
    return {"output": "my-output"}

# Define your dataset
dataset_name = "my-dataset"

# Run the evaluation
evaluate(
    my_model,
    data=dataset_name,
    evaluators=["qa"],
    experiment_prefix="my-experiment",
)
```

### 4. Monitoring

LangSmith provides monitoring dashboards that allow you to track the performance of your applications over time.

### 5. Hub

The LangSmith Hub is a central repository for sharing and discovering prompts, chains, and other LangChain components.

**Code Snippet:**

```python
from langchain import hub

# Pull a prompt from the Hub
prompt = hub.pull("efriis/my-first-prompt")

# Use the prompt in your application
# ...
```
