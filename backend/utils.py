import requests
from bs4 import BeautifulSoup
from .models import InstagramSession

def get_instagram_bio(username, user):
    try:
        session = InstagramSession.objects.get(user=user)
        cookies = {"sessionid": session.sessionid}
    except InstagramSession.DoesNotExist:
        return "No session ID found for user"

    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", text=lambda t: t and "biography" in t)
            if script_tag:
                bio_start = script_tag.text.find('"biography":"') + len('"biography":"')
                bio_end = script_tag.text.find('"', bio_start)
                return script_tag.text[bio_start:bio_end] if bio_start and bio_end else "No description found"
        return f"Failed to fetch description, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {str(e)}"
