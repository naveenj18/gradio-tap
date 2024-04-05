import requests

API_URL = "http://localhost:3000/api/v1/prediction/d3e596bb-9bf2-48c4-972e-05cb47863310"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})