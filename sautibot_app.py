import streamlit as st
from datetime import datetime
from streamlit_chat import message
import time
import pandas as pd
import re
import csv
import uuid
import os

st.set_page_config(page_title="SautiBot", page_icon="💬", layout="centered")

# Initialize session state
if "anonymous" not in st.session_state:
    st.session_state.anonymous = False
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "👋 Hi there, how can I support you today?"}]
if "responses" not in st.session_state:
    st.session_state.responses = pd.read_csv("chatbot_response_templates.csv")
if "last_offer" not in st.session_state:
    st.session_state.last_offer = None
if "session_id" not in st.session_state:
    st.session_state.session_id = f"anon_{str(uuid.uuid4())[:8]}"

# Emergency detection keywords
emergency_keywords = [
    "rape", "raped", "stubbed", "knife", "bleeding", "beat", "abuse", "unsafe", "danger", "emergency",
    "molest", "harass", "blood", "die", "help", "suicide", "kill", "burn", "stab", "injury", "hurt"
]

# Logging function
def log_message(role, content):
    is_emergency = any(word in content.lower() for word in emergency_keywords)
    log_file = "chat_logs.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "session_id", "role", "message", "emergency"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            st.session_state.session_id,
            role,
            content,
            "Yes" if is_emergency else "No"
        ])

# Background styling
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        body {
            background-image: url('https://images.unsplash.com/photo-1536104968055-4d61aa56f46a?auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
        }
        .footer {
            text-align: center;
            color: #eee;
            font-size: 13px;
            padding-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("### 🛡️ SautiBot (Anonymous Mode)" if st.session_state.anonymous else "### 🛡️ SautiBot")
st.markdown("*You're now chatting anonymously.*" if st.session_state.anonymous else "*Your Safe Space. Your Voice. Your Power.*")

# Quick Help Buttons
st.markdown("#### 💬 Quick Help Options")
col1, col2, col3 = st.columns(3)
trigger_input = None
if col1.button("🚨 Report Abuse"):
    trigger_input = "I want to report abuse"
if col2.button("😨 I Feel Unsafe"):
    trigger_input = "I feel unsafe right now"
if col3.button("👨‍🦱 I'm a Man & I Need Help"):
    trigger_input = "I'm a man and I need help"

# Show chat history
for i, msg in enumerate(st.session_state.messages):
    is_user = msg["role"] == "user"
    message(msg["content"], is_user=is_user, key=f"msg-{i}")

# Response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    greetings = ["hi", "hello", "hey"]
    confirmations = ["yes", "please", "okay", "sure", "alright", "sawa", "ndio"]

    if any(greet in user_input for greet in greetings):
        return "Hello, how may I help you today?"

    if st.session_state.last_offer == "support" and user_input.strip() in confirmations:
        st.session_state.last_offer = None
        return "📞 You can call Usikimye at +254 110 000 999 or [chat with them on WhatsApp](https://wa.me/254110000999)."

    for _, row in st.session_state.responses.iterrows():
        keywords = str(row['keywords']).lower().split(';')
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", user_input):
                if pd.notna(row['response']) and row['response'].strip() != "":
                    if "connect" in row['response'].lower() or "call" in row['response'].lower():
                        st.session_state.last_offer = "support"
                    return row['response']

    return "I'm here for you. Could you share a little more so I can better support you?"

# Typing effect
def typing_reply(text):
    with st.spinner("SautiBot is typing..."):
        time.sleep(1.2)
    i = len(st.session_state.messages)
    message(text, is_user=False, key=f"msg-{i}")

# Input area
user_input = st.chat_input("Type your message here...")
final_input = trigger_input or user_input

if final_input and final_input.strip() != "":
    st.session_state.messages.append({"role": "user", "content": final_input.strip()})
    log_message("user", final_input.strip())
    message(final_input.strip(), is_user=True, key=f"msg-{len(st.session_state.messages)}")

    bot_response = get_bot_response(final_input.strip())
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    log_message("bot", bot_response)
    typing_reply(bot_response)

# Sidebar
with st.sidebar:
    st.markdown("### 🚨 Emergency Help")
    st.markdown("[📞 Call 911](tel:911)", unsafe_allow_html=True)
    st.markdown("[📱 Call Usikimye](tel:+254110000999)", unsafe_allow_html=True)
    st.markdown("[💬 WhatsApp Support](https://wa.me/254110000999)", unsafe_allow_html=True)

    if st.button("🕶️ Switch to Anonymous Mode"):
        st.session_state.anonymous = True
        st.session_state.messages = [{"role": "bot", "content": "🕶️ You're now in anonymous mode. How can I support you?"}]
        st.rerun()

    if st.button("🤝 Talk to a Support Person"):
        st.markdown("We're connecting you now... [💬 Chat via WhatsApp](https://wa.me/254110000999)", unsafe_allow_html=True)
        st.markdown("📱 Save this number: **+254 110 000 999**")

    # Download log
    if os.path.exists("chat_logs.csv"):
        with open("chat_logs.csv", "rb") as file:
            st.download_button("⬇️ Download Chat Logs", file, file_name="chat_logs.csv", mime="text/csv")

    st.markdown("---")
    st.caption("📱 *Mobile tap-to-call works best on phones.*")

# Footer
st.markdown('<div class="footer">Made with ❤️ by Berlyn Mumbua</div>', unsafe_allow_html=True)
