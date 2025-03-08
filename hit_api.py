import requests

def sendRequest(url_name, token):
    url = url_name
    headers = {
        "Accept": "application/json",
        "Private-Token": token }
    response = requests.get(url, headers=headers)
    return response
    

def getResponse(api_response):
    if api_response.status_code == 200:
        response_data = api_response.json()
        return(response_data)
    else:
        print(f"Failed to retrieve response with status code: {api_response.status_code}")



url = "https://gitlab.boon.com.au/api/v4/projects"
private_token = "personalY5x4w3Cme8yqUjMoxmyi"

response = sendRequest(url, private_token)

result = getResponse(response)
print(result)

