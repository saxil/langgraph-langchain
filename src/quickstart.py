

import os
from langchain_openai import ChatOpenAI

# IMPORTANT: Replace "your-openai-api-key" with your actual OpenAI API key
# For security, it's best to set this as a system environment variable.
# On Windows, you can set it with: setx OPENAI_API_KEY "your-openai-api-key"
# On macOS/Linux, use: export OPENAI_API_KEY="your-openai-api-key"
# If you are setting it in the script like below, make sure this file is not publicly exposed.
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 1. Initialize the LLM
# We are using the ChatOpenAI class with the "gpt-3.5-turbo" model.
# The temperature is set to 0 to get more deterministic and less random responses.
try:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # 2. Create a prompt
    # This is the question or instruction we want to send to the model.
    prompt = "What are the top 3 benefits of using LangChain for AI development?"

    # 3. Invoke the model
    # The `invoke` method sends the prompt to the LLM and gets the response.
    response = llm.invoke(prompt)

    # 4. Print the result
    print("--- LangChain Quickstart Response ---")
    print(response.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print("\n--- Troubleshooting ---")
    print("1. Make sure you have replaced 'your-openai-api-key' with a valid key.")
    print("2. Ensure the 'langchain' and 'langchain-openai' packages are installed (`pip install langchain langchain-openai`).")
    print("3. Check your internet connection and OpenAI account status.")


