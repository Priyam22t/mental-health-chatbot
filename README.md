# Mental Health Support Chatbot 💬

A web-based mental health support chatbot built using Flask, HTML, and CSS
The application is designed with ethical mental-health principles, offering supportive, non-judgmental conversations, crisis keyword detection, and a calm chat-based user interface.

The chatbot works with or without an AI API key. When AI services are unavailable, it gracefully falls back to emotion-aware, rule-based responses to ensure reliability and safety.

---

## 🌟 Features

- 💬 Chat-style user interface with chat bubbles
- 🌙 Light/Dark mode toggle
- 🧠 Emotion-aware responses (stress, anxiety, sadness, loneliness)
- 🚨 Crisis and self-harm keyword detection
- 📞 Helpline guidance for users in distress
- 🔁 Randomized supportive responses (no repetition)
- 🛡️ Safe fallback logic when AI API quota is exceeded
- 🎓 Suitable for college projects, demos, and portfolios

---

## 🛠️ Tech Stack

- Backend: Python (Flask)
- Frontend: HTML, CSS
- Optional AI Integration: OpenAI API
- Environment Management: python-dotenv

---

## 📁 Project Structure

mental-health-chatbot/
│── app.py  
│── .env  
│── templates/  
│   └── index.html  
│── static/  
│   └── style.css  

---

## ⚙️ Setup Instructions

1. Clone the repository:
   git clone <your-repo-link>

2. Navigate to the project folder:
   cd mental-health-chatbot

3. Create and activate a virtual environment (optional but recommended)

4. Install dependencies:
   pip install flask python-dotenv openai

5. Create a `.env` file in the root directory:
   OPENAI_API_KEY=your_api_key_here

   ⚠️ Do not add quotes and never upload this file to GitHub.

6. Run the application:
   python app.py

7. Open your browser and visit:
   http://127.0.0.1:5000

---

## 🧪 Testing Examples

- Hello
- I feel stressed and overwhelmed
- I feel anxious about my future
- I feel lonely
- I feel very low today
- I want to hurt myself (tests crisis detection)

---

## 🛡️ Mental Health Safety Notice

This chatbot is NOT a replacement for professional therapy or medical advice.  
It is intended for educational and supportive purposes only.  
In cases of severe distress, users are encouraged to seek help from trained professionals or local emergency services.

---

## 🚀 Future Improvements

- Online deployment (Render / Railway)
- User authentication
- Mood tracking over time
- Guided breathing or grounding exercises
- Multilingual support

---

## 📄 License

This project is for educational purposes.  
You are free to modify and improve it with proper attribution.

---

## 🙌 Acknowledgements

Built with a focus on empathy, accessibility, and ethical mental-health design.
