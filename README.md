## Integration of a Mathematical Calulations with a Chat Completion System using LLM Function-Calling

### AIM:
To design and implement a Python function for calculating the volume of a cylinder, integrate it with a chat completion system utilizing the function-calling feature of a large language model (LLM).

### PROBLEM STATEMENT:
This Python script integrates OpenAI's GPT-3.5 Turbo model to calculate the volume of a cylinder based on user input. It defines a function calculate_cylinder_volume(radius, height) to compute the volume and formats the output as JSON. The script simulates an AI-driven interaction where the user queries the cylinder's volume, and the AI, using function calling, retrieves and processes the required values before returning the result.
### DESIGN STEPS:

#### STEP 1:
Setup and Import Dependencies: Import libraries and load OpenAI API key using dotenv.

#### STEP 2:
Define Volume Calculation Function: Compute cylinder volume and return JSON output.

#### STEP 3:
Configure OpenAI Function Calling: Define function schema for AI to recognize and call correctly.

#### STEP 4:
Simulate AI Interaction: Create user query, send it to OpenAI, and check for function execution.

#### STEP 5:
Process and Return Response: Extract parameters, compute volume, update messages, and generate final AI response.

### PROGRAM:
```
import os
import openai
import json
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
def calculate_cylinder_volume(radius, height):
    volume = 3.14159265359 * (radius ** 2) * height
    return json.dumps({"radius": radius, "height": height, "volume": volume})
functions = [
    {
        "name": "calculate_cylinder_volume",
        "description": "Calculate the volume of a cylinder given its radius and height.",
        "parameters": {
            "type": "object",
            "properties": {
                "radius": {"type": "number", "description": "The radius of the cylinder in meters."},
                "height": {"type": "number", "description": "The height of the cylinder in meters."}
            },
            "required": ["radius", "height"]
        }
    }
]
messages = [{"role": "user", "content": "What is the volume of a cylinder with radius 7 and height 10?"}]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)
response_message = response["choices"][0]["message"]
if "function_call" in response_message:
    args = json.loads(response_message["function_call"]["arguments"])
    result = calculate_cylinder_volume(**args)
messages.append({
    "role": "function",
    "name": "calculate_cylinder_volume",
    "content": result,
})
final_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
print(final_response["choices"][0]["message"]["content"])
```

### OUTPUT:
![image](https://github.com/user-attachments/assets/29e43780-cc44-446f-a857-c599e620bc41)

### RESULT:
The code enables LLM-driven cylinder volume calculation via function calling.
