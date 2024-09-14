import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def github_request(method, url, data=None):
    try:
        response = requests.request(method, url, json=data, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}, status code: {response.status_code}")
    except Exception as err:
        print(f"Error: {err}")
    return None

def create_repository(repo_name):
    url = f"{GITHUB_API_URL}/user/repos"
    data = {"name": repo_name, "private": False, "auto_init": True}
    response = github_request("POST", url, data)
    if response and response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    return response

def repository_exists(repo_name):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response = github_request("GET", url)
    if response and response.status_code == 200:
        print(f"Repository '{repo_name}' exists.")
        return True
    print(f"Repository '{repo_name}' does not exist.")
    return False

def delete_repository(repo_name):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response = github_request("DELETE", url)
    if response and response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    return response

if __name__ == "__main__":
    if create_repository(REPO_NAME):
        if repository_exists(REPO_NAME):
            delete_repository(REPO_NAME)
