import requests

api_url = "http://shipbe.online/api/shibes?count=1"

response = requests.get(api_url)

# note this endpoint is no longer live so this doesn't work.
status_code = response.status_code
print(f"status code: {status_code}")

response_json = response.json()

print(response_json)