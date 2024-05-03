import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_response(prompt, max_tokens=100):
    """Generate a response using the OpenAI API."""
    response = client.chat.completions.create(
         messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    max_tokens=max_tokens,
    n=1,
    stop=None,
    temperature=0.7,
    )
    
    content = response.choices[0].message.content.strip()  
    return content