import json
import os
import requests

from typing import List, Union

def call_bot(question : str):
    # Replace YOUR_API_KEY with your OpenAI API key
    apiKey = ""

    # Set the model to use
    model = "text-davinci-003"

    maxTokens = 4000 

    # Build the request body
    requestBody = json.dumps({"model": model, "prompt": question, "temperature": 1, "max_tokens": maxTokens})

    headers = {"Content-Type": "application/json", "Authorization": "Bearer "+apiKey}

    # Send the request
    res = requests.post("https://api.openai.com/v1/completions", data=requestBody, headers=headers)

    # Read the response
    responseBody = json.loads(res.text)

    return responseBody["choices"][0]["text"]