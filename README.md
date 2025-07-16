# 🛡️ SautiBot – AI-Powered Support for Survivors of Abuse

A compassionate AI chatbot built with **Streamlit**, designed to support individuals facing **abuse, violence, or emotional distress**, by providing anonymous assistance and connecting users to local crisis support services.

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue)](https://sautibotapppy-zx7cqciusxpnqbb5f5zsmw.streamlit.app/)
[![UN SDGs](https://img.shields.io/badge/UN%20SDGs-3%20&%2016-green)](https://sdgs.un.org/goals)
[![MIT License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 🌍 SDG Alignment

**Primary Goals:**

- **SDG 3 – Good Health and Well-being**  
  *Ensure healthy lives and promote well-being for all at all ages.*

- **SDG 16 – Peace, Justice and Strong Institutions**  
  *Promote peaceful and inclusive societies, access to justice, and strong institutions.*

---

## 💡 Problem Statement

Many individuals face **domestic violence, abuse, and emotional trauma** but lack access to **confidential, safe, and immediate support channels**. Stigma, fear, and limited resources often prevent them from seeking help.

---

## 🤖 AI Solution

SautiBot uses **keyword-matching NLP**, intelligent logic, and an empathetic design to:

- Listen anonymously
- Respond compassionately
- Identify keywords related to abuse, mental health, or danger
- Offer tailored, culturally-sensitive responses
- Connect users to verified support like **Usikimye** or **emergency numbers**

---

## 🧪 Software Engineering Concepts Applied

| Concept            | Application in Project                             |
|--------------------|-----------------------------------------------------|
| **Automation**     | Auto-matching user messages to categorized responses |
| **Modular Code**   | Split into logic blocks: UI, keyword engine, memory |
| **Version Control**| Managed on GitHub using Git                        |
| **Ethical Design** | Anonymity toggle, sensitive language handling       |
| **Testing**        | Manual testing for logic coverage and edge cases    |

---

## 🚀 Live App

Access the deployed app here:  
🔗 [https://sautibotapppy-zx7cqciusxpnqbb5f5zsmw.streamlit.app/](https://sautibotapppy-zx7cqciusxpnqbb5f5zsmw.streamlit.app/)

---

## ⚙️ How It Works

1. User interacts through a simple chat interface.
2. The chatbot parses input and scans for sensitive keywords.
3. Based on the match, it replies with tailored support, empathy, and resources.
4. It offers the option to connect to **emergency lines** or **organizations** like Usikimye.
5. Anonymous mode available for safety.

---

## 📂 Project Structure

sautibot/
├── app/
│ └── sautibot_app.py # Main Streamlit app
├── data/
│ └── chatbot_response_templates.csv # Keyword-response pairs
├── docs/
│ ├── final_report.docx # Formal project report
│ └── pitch_deck.pdf # Optional: slide presentation
├── requirements.txt
├── README.md
└── .gitignore

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/mumbua-mutinda/sautibot.git
cd sautibot

### 2. Create & activate virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate  # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the Streamlit app
streamlit run app/sautibot_app.py

---

📈 Example Keywords
"rape", "molested", "beaten", "unsafe", "depressed"

"stubbed", "harassed", "anxious", "sad", "panic"

"teacher", "uncle", "aunt", "partner", "husband"

Also includes Swahili variations: "nateswa", "nanyanyaswa", "nisaidie", etc.

---

☎️ Emergency Contacts
The bot offers:

📞 Call Usikimye: +254 110 000 999

💬 WhatsApp Chat with Usikimye

🚨 Emergency: Dial 911 or 1199 in Kenya

---

📜 License
MIT License — feel free to adapt this for good causes!

---

🙌 Acknowledgments
Usikimye

Streamlit

Kenya’s local mental health and GBV response initiatives




