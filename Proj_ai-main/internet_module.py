import requests

def get_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def post_request(url, data=None, headers=None):
    try:
        response = requests.post(url, json=data, headers=headers, timeout=5)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"