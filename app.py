import requests

# Base URL for Emoji Hub API
BASE_URL = "https://emojihub.yurace.pro/api"

def get_random_emoji():
    """
    Get a random emoji from the Emoji Hub API.
    """
    try:
        response = requests.get(f"{BASE_URL}/random")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve random emoji. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_random_emoji_by_category(category: str):
    """
    Get a random emoji from a specific category.
    """
    try:
        response = requests.get(f"{BASE_URL}/random/category/{category}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve random emoji from category '{category}'. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_random_emoji_by_group(group: str):
    """
    Get a random emoji from a specific group.
    """
    try:
        response = requests.get(f"{BASE_URL}/random/group/{group}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve random emoji from group '{group}'. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_all_emojis():
    """
    Get all emojis from the Emoji Hub API.
    """
    try:
        response = requests.get(f"{BASE_URL}/all")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve all emojis. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_emojis_by_category(category: str):
    """
    Get all emojis from a specific category.
    """
    try:
        response = requests.get(f"{BASE_URL}/all/category/{category}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve emojis from category '{category}'. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_emojis_by_group(group: str):
    """
    Get all emojis from a specific group.
    """
    try:
        response = requests.get(f"{BASE_URL}/all/group/{group}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve emojis from group '{group}'. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
