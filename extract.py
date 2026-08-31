import requests
import json
import os


topic = input("Enter a topic to search GitHub repositories: ")

url = f"https://api.github.com/search/repositories?q={topic}&sort=stars&per_page=100"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    repositories = data["items"]

    os.makedirs("data/raw", exist_ok=True)

    with open(
        "data/raw/repositories.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(repositories, file, indent=4)

    print("Data extracted successfully!")
    print("Total repositories collected:", len(repositories))

else:
    print("Error:", response.status_code)