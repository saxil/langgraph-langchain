
# LangChain

LangChain is an open-source framework for developing applications powered by large language models (LLMs). It provides a modular architecture and a set of tools that simplify the process of building complex AI applications.

## Core Components

LangChain is built around several key components:

### 1. Models

LangChain provides a standardized interface for interacting with various LLMs and embedding models.

**Code Snippet:**

```python
from langchain_openai import ChatOpenAI

# Initialize an OpenAI chat model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Invoke the model with a prompt
response = llm.invoke("What is the capital of France?")

print(response)
```

### 2. Prompts

Prompts are the inputs given to LLMs. LangChain provides tools for creating and managing prompts, including prompt templates and example selectors.

**Code Snippet:**

```python
from langchain.prompts import PromptTemplate

# Create a prompt template
prompt_template = PromptTemplate.from_template(
    "What is the capital of {country}?"
)

# Format the template with a value
prompt = prompt_template.format(country="Germany")

print(prompt)
```

### 3. Chains

Chains allow you to combine multiple LLM calls or calls to other tools in a sequence.

**Code Snippet:**

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the model and prompt template
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
prompt_template = PromptTemplate.from_template(
    "What is a good name for a company that makes {product}?"
)

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the chain with an input
response = chain.run(product="colorful socks")

print(response)
```

### 4. Agents

Agents use an LLM to decide which actions to take. They can use tools to interact with the outside world, such as search engines or APIs.

**Code Snippet:**

```python
from langchain_community.agent_toolkits import create_python_agent
from langchain_community.tools.python.tool import PythonREPLTool
from langchain_openai import OpenAI

# Initialize the LLM and tools
llm = OpenAI(temperature=0)
tools = [PythonREPLTool()]

# Create an agent
agent = create_python_agent(llm=llm, tool=tools, agent_executor_kwargs={"handle_parsing_errors": True})

# Run the agent with a prompt
response = agent.run("What is 2 + 2?")

print(response)
```

### 5. Indexes

Indexes are used to structure and retrieve data. They are essential for making applications data-aware, enabling them to answer questions about specific documents or knowledge bases.

**Code Snippet:**

```python
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# Load a document
loader = TextLoader('document.txt')

# Create an index from the document
index = VectorstoreIndexCreator().from_loaders([loader])

# Query the index
response = index.query("What is the main topic of the document?")

print(response)
```

### 6. Memory

Memory allows applications to remember previous interactions, which is crucial for chatbots and other conversational AI.

**Code Snippet:**

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI

# Initialize the LLM and memory
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

# Have a conversation
print(conversation.run("Hi, I'm Sahil."))
print(conversation.run("What's my name?"))
```
