import requests

url = "https://jsearch.p.rapidapi.com/search"

headers = {
    "x-rapidapi-key": "0d77a203cbmsh8524430bb9d7ea0p105dfdjsnf490531c04f2",
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

params = {"query": "python developer", "num_pages": "1"}

res = requests.get(url, headers=headers, params=params)

print("STATUS:", res.status_code)
print("RAW RESPONSE:", res.json())
