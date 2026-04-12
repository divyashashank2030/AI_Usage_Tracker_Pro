import requests
from app.utils.config import DEEPGRAM_API_KEY

def get_stt_usage():
    try:
        headers = {
            "Authorization": f"Token {DEEPGRAM_API_KEY}"
        }

        response = requests.get(
            "https://api.deepgram.com/v1/projects",
            headers=headers
        )

        if response.status_code != 200:
            return {
                "provider": "Deepgram",
                "status": "error",
                "message": response.text
            }

        data = response.json()

        return {
            "provider": "Deepgram",
            "status": "success",
            "projects_count": len(data.get("projects", []))
        }

    except Exception as e:
        return {
            "provider": "Deepgram",
            "status": "error",
            "message": str(e)
        }
