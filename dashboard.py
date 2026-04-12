import streamlit as st
import requests
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Usage Dashboard", layout="wide")

# 🔹 Title & Description
st.markdown("## AI Usage Tracker Dashboard")
st.markdown("Monitor usage across multiple AI providers in one place")

# 🔹 Sidebar - Auto Refresh
refresh_interval = st.sidebar.slider("Auto Refresh (seconds)", 5, 60, 10)

placeholder = st.empty()

while True:
    with placeholder.container():

        # 🔹 Fetch Data
        try:
            response = requests.get("http://127.0.0.1:8000/dashboard")
            data = response.json()
        except:
            st.error("Backend not running")
            st.stop()

        # 🔹 Overall Summary
        st.subheader("Overall Summary")

        total_services = 3
        working_services = 0

        if data.get("openai", {}).get("status") in ["success", "partial"]:
            working_services += 1

        if data.get("tts", {}).get("status") in ["success", "partial"]:
            working_services += 1

        if data.get("stt", {}).get("status") == "success":
            working_services += 1

        st.success(f"{working_services}/{total_services} Services Operational")

        st.divider()

        col1, col2, col3 = st.columns(3)

        # ------------------ OPENAI ------------------
        with col1:
            st.subheader("OpenAI")

            openai = data.get("openai", {})

            if openai["status"] == "partial":
                usage = openai["usage"]

                st.metric("Tokens Used", usage["tokens_used"])
                st.metric("Estimated Cost ($)", usage["estimated_cost"])

                st.info(openai["note"])

                df = pd.DataFrame({
                    "Metric": ["Tokens Used"],
                    "Value": [usage["tokens_used"]]
                })
                st.bar_chart(df.set_index("Metric"))

            else:
                st.error(openai.get("message", "Error"))

        # ------------------ ELEVENLABS ------------------
        with col2:
            st.subheader("ElevenLabs (TTS)")

            tts = data.get("tts", {})

            if tts["status"] in ["success", "partial"]:
                usage = tts["usage"]

                voices = usage.get("available_voices", 0)

                st.metric("Available Voices", voices)
                st.info(tts.get("note", ""))

                df = pd.DataFrame({
                    "Metric": ["Voices"],
                    "Value": [voices]
                })
                st.bar_chart(df.set_index("Metric"))

            else:
                st.error(tts.get("message", "Error"))

        # ------------------ DEEPGRAM ------------------
        with col3:
            st.subheader("Deepgram (STT)")

            stt_data = data.get("stt", {})

            if stt_data["status"] == "success":
                projects = stt_data["projects_count"]

                st.metric("Projects", projects)

                df = pd.DataFrame({
                    "Metric": ["Projects"],
                    "Value": [projects]
                })
                st.bar_chart(df.set_index("Metric"))

            else:
                st.error(stt_data.get("message", "Error"))

        st.divider()

        # 🔹 Footer
        st.caption("Auto-refreshing dashboard...")
        st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    time.sleep(refresh_interval)