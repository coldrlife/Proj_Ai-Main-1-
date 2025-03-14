import requests

def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON data
    else:
        return f"Error: {response.status_code}"

# Example usage
if __name__ == "__main__":
    api_url = "https://api.github.com"  # Example: GitHub API
    data = fetch_data_from_api(api_url)
    print(data)