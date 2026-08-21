import requests

URL = "https://api.github.com/users/PashMaak"

r = requests.get(URL)

if (r.status_code // 100 == 2):
    data = r.json()
    print("Nomu Nasab: ", data["name"])
    print("Amount of reps: ", data["public_repos"])
else:
    print(f"Status code {r.status_code}")