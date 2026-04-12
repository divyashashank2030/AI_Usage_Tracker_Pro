import requests
from app.utils.config import ELEVENLABS_API_KEY

def get_tts_usage():
    try:
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY
        }

        # Use voices endpoint (no permission issue)
        response = requests.get(
            "https://api.elevenlabs.io/v1/voices",
            headers=headers
        )

        if response.status_code != 200:
            return {
                "provider": "ElevenLabs",
                "status": "error",
                "message": response.text
            }

        data = response.json()
        voices = data.get("voices", [])

        return {
            "provider": "ElevenLabs",
            "status": "partial",
            "usage": {
                "available_voices": len(voices)
            },
            "note": "User billing API restricted. Showing available voices instead."
        }

    except Exception as e:
        return {
            "provider": "ElevenLabs",
            "status": "error",
            "message": str(e)
        }




# import requests
# from app.utils.config import ELEVENLABS_API_KEY

# def get_tts_usage():
#     try:
#         headers = {
#             "xi-api-key": ELEVENLABS_API_KEY
#         }

#         response = requests.get(
#             "https://api.elevenlabs.io/v1/user",
#             headers=headers
#         )

#         if response.status_code != 200:
#             return {
#                 "provider": "ElevenLabs",
#                 "status": "error",
#                 "message": response.text
#             }

#         data = response.json()
#         sub = data.get("subscription", {})

#         used = sub.get("character_count", 0)
#         total = sub.get("character_limit", 0)

#         return {
#             "provider": "ElevenLabs",
#             "status": "success",
#             "usage": {
#                 "used_characters": used,
#                 "total_characters": total,
#                 "remaining_characters": total - used
#             }
#         }

#     except Exception as e:
#         return {
#             "provider": "ElevenLabs",
#             "status": "error",
#             "message": str(e)
#         }
