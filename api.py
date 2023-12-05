import requests
import json

url = "https://gww-aitestpilots.openai.azure.com/openai/deployments/Story_Refinement_Experimental/chat/completions?api-version=2023-07-01-preview"

payload = json.dumps({
  "messages": [
    {
      "role": "system",
      "content": "Hello World"
    },
    {
      "role": "user",
      "content": "Foo Bar"
    },
    {
      "role": "assistant",
      "content": "Hello Mars"
    },
    {
      "role": "user",
      "content": "Our login page should show an error when we enter the incorrect password."
    },
    {
      "role": "assistant",
      "content": "Foo Bar"
    }
  ],
  "max_tokens": 800,
  "temperature": 0.7,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "top_p": 0.95,
  "stop": None
})
headers = {
  'Content-Type': 'application/json',
  'api-key': 'YOUR_API_KEY',
  'Authorization': 'Bearer token'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
