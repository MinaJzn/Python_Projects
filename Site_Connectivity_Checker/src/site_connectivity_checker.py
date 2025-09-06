import requests


def format_url(url : str)-> str:
    """
    Formats a given URL into a standard format starting with 'https://www.'.

    This function:
    - Removes leading/trailing whitespace.
    - Strips 'http://', 'https://', or 'www.' if present.
    - Ensures the final URL begins with 'https://www.'.
    
    Returns:A formatted URL with 'https://www.' prefix.
    """
    url = url.strip()
    
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
    
    if url.startswith('www.'):
        url = url[len('www.'):]
    
    formatted_url = 'https://www.' + url
    return formatted_url

def check_site_connectivity(url : str)-> tuple:
    """
    Checks if a website is reachable by sending an HTTP GET request.

    This function:
    - Sends a GET request to the given URL with a common browser user-agent.
    - Uses a timeout of 5 seconds to avoid long waits.
    - Returns a message based on the HTTP status code or any request exceptions.

    Returns: A tuple containing the original URL and a message indicating:
            - ✅ If the site is up (HTTP 200).
            - ⚠️ If the site is down (non-200 status).
            - ❌ If the request failed due to network issues or invalid URL.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, timeout=5, headers=headers)

        if response.status_code == 200:
            return url, f"✅ {url} is up!"
        else:
            return url, f"⚠️ {url} is down. Status Code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return url, f"❌ Failed to reach {url}. Error: {e}"
    


