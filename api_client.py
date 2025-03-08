import json
import requests

# Login to get the token
login_url = "http://127.0.0.1:8000/token"
login_data = {
    "username": "nandiya",
    "token": "personalY5x4w3Cme8yqUjMoxmyi"
}

response = requests.post(login_url, data=login_data)

# Check if the response was successful
if response.status_code == 200:
    access_token = response.json().get("access_token")
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get token: {response.status_code}, {response.text}")

# # Use the token to access the /projects endpoint
projects_url = "http://127.0.0.1:8000/projects"
headers = {"Authorization": f"Bearer {access_token}"}
project_response = requests.get(projects_url, headers=headers)

insert_url = "http://127.0.0.1:8000/insert_projects/"
response = requests.post(projects_url, json_string=project_response)

# Handle the response
if response.status_code == 200:
    print("Project inserted successfully!")
    print("Response:", response.json())
else:
    print("Failed to insert project!")
    print("Status Code:", response.status_code)
    print("Response:", response.json())



