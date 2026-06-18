import requests

def check_website_status():
    # This uses our new dependency to check a website
    response = requests.get("https://httpbin.org")
    return response.status_code

if __name__ == "__main__":
    status = check_website_status()
    print(f"Website responded with status code: {status}")
