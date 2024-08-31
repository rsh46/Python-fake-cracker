import requests
import json

# API Key from api-ninjas.com
API_KEY = "7BOxQ4GRgWKhp8OZ6LplpQ==dVuwsKPv3BVeWE0K"

def get_opposite(word):
    api_url = f"https://api.api-ninjas.com/v1/thesaurus?word={word}"
    headers = {"X-Api-Key": "7BOxQ4GRgWKhp8OZ6LplpQ==dVuwsKPv3BVeWE0K"}
  # Use the API_KEY variable
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        opposites = [item for item in data["results"] if item["relationship"] == "antonym"]
        if opposites:
            return opposites[0]["word"]
        else:
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None

def chatbot():
    print("Welcome to the Opposite Chatbot!")
    print("---------------------------------")
    while True:
        print("You: ", end="")
        user_input = input()
        if len(user_input.split()) > 1:
            print("Invalid input. Please enter a single word.")
            continue
        opposite = get_opposite(user_input)
        if opposite:
            print(f"Bot: The opposite of {user_input} is {opposite}.")
        else:
            print(f"Bot: Sorry, no opposite found for {user_input}.")
        print()

if __name__ == "__main__":
    chatbot()
