#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
import openai
import json
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY") 


# In[17]:


def calculate_cylinder_volume(radius, height):
    volume = 3.14159265359 * (radius ** 2) * height
    return json.dumps({"radius": radius, "height": height, "volume": volume})


# In[18]:


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



# In[19]:


messages = [{"role": "user", "content": "What is the volume of a cylinder with radius 7 and height 10?"}]


# In[20]:


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    functions=functions
)


# In[21]:


response_message = response["choices"][0]["message"]
if "function_call" in response_message:
    args = json.loads(response_message["function_call"]["arguments"])
    result = calculate_cylinder_volume(**args)


# In[22]:


messages.append({
    "role": "function",
    "name": "calculate_cylinder_volume",
    "content": result,
})


# In[23]:


final_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
print(final_response["choices"][0]["message"]["content"])


# In[ ]:




