import requests

HEADERS = {
    "X-API-Key": '3f4657b882bc400bb55ba363030f48db'
}

xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"
print("\n\n\nConnecting to Bungie: " + xur_url + "\n")
print("Fetching data for: Xur's Inventory!")

res = requests.get(xur_url, headers=HEADERS)
error_status = res.json()['ErrorStatus']
print("Error status: " + error_status + "\n")
