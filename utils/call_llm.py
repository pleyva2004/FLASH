from openai import OpenAI
import dotenv
import os

def call_llm(messages):
    dotenv.load_dotenv()

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test the LLM call

    messages =  "In a few words, what's the meaning of life?"
    formatted_messages = [{"role": "user", "content": messages}]
    response = call_llm(formatted_messages)
    print(f"Prompt: {messages}")
    print(f"Response: {response}")