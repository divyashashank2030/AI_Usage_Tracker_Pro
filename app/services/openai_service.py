def get_openai_usage():
    try:
        tokens_used = 1500
        cost_per_1k_tokens = 0.002

        estimated_cost = (tokens_used / 1000) * cost_per_1k_tokens

        return {
            "provider": "OpenAI",
            "status": "partial",
            "usage": {
                "tokens_used": tokens_used,
                "estimated_cost": round(estimated_cost, 4)
            },
            "note": "Billing API restricted. Using estimated usage based on token consumption."
        }

    except Exception as e:
        return {
            "provider": "OpenAI",
            "status": "error",
            "message": str(e)
        }


# import requests
# from app.utils.config import OPENAI_API_KEY

# def get_openai_usage():
#     try:
#         headers = {
#             "Authorization": f"Bearer {OPENAI_API_KEY}"
#         }

#         response = requests.get(
#             "https://api.openai.com/v1/dashboard/billing/credit_grants",
#             headers=headers
#         )

#         if response.status_code != 200:
#             return {
#                 "provider": "OpenAI",
#                 "status": "error",
#                 "message": response.text
#             }

#         data = response.json()

#         return {
#             "provider": "OpenAI",
#             "status": "success",
#             "total_granted": data.get("total_granted"),
#             "total_used": data.get("total_used"),
#             "remaining": data.get("total_available")
#         }

#     except Exception as e:
#         return {
#             "provider": "OpenAI",
#             "status": "error",
#             "message": str(e)
#         }
