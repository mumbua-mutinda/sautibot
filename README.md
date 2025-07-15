# 🛡️ SautiBot – AI-Powered Support Chatbot for Survivors (SDG 3 & 16)

**SautiBot** is a mental health and safety support chatbot designed to provide confidential, empathetic responses to individuals experiencing abuse, violence, or emotional distress. Built with Streamlit, it combines natural language detection, ethical AI principles, and accessible design to support Sustainable Development Goals:

- 🎯 **SDG 3** – Good Health and Well-being  
- 🎯 **SDG 16** – Peace, Justice, and Strong Institutions

---

## 💡 Features

- 🤖 Keyword-based support system (e.g., rape, violence, depression)
- 🌐 Swahili + English response capability
- 🕶️ Anonymous mode for safe disclosure
- 📞 Emergency contact integration (e.g., Usikimye, 1199, 911)
- 📁 CSV-driven responses for flexibility and localization

---

## 🧠 Tech Stack

| Category              | Tools Used                            |
|----------------------|----------------------------------------|
| Frontend              | [Streamlit](https://streamlit.io)      |
| Language Detection    | Custom regex on keywords from CSV     |
| Dataset               | `chatbot_response_templates.csv`       |
| Deployment (Optional) | [Streamlit Cloud](https://share.streamlit.io) |
| Repo & Version Control | Git + GitHub                         |

---

## 🧪 How to Run

```bash
git clone https://github.com/mumbua-mutinda/sautibot.git
cd "sautibot AI project"
pip install -r requirements.txt
streamlit run sautibot_app.py
---

📊 SDG Alignment
SDG	How It’s Addressed
SDG 3	Promotes mental health & access to urgent support
SDG 16	Supports peaceful and inclusive communities via safe reporting

✅ Ethical AI Practices
✅ Inclusive, non-judgmental language

✅ Gender-neutral & trauma-informed responses

✅ Minimal data retention (no user logging in local version)

✅ Works in low-resource settings (no cloud dependency)

❤️ Built By
Berlyn Mumbua – AI for Software Engineering Student

“Your Safe Space. Your Voice. Your Power.”

🔗 Contact & Help Resources
📞 Usikimye Kenya: +254 110 000 999

📱 WhatsApp: Chat Usikimye

🚨 Emergency (Kenya): Call 1199 or 911
