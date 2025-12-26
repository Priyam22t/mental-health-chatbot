from flask import Flask, render_template, request
import random

app = Flask(__name__)

chat_history = []

# Crisis keywords (highest priority)
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "self harm", "end my life",
    "want to die", "hurt myself", "no reason to live"
]

# Emotion-based response pools
STRESS_RESPONSES = [
    "It sounds like you're under a lot of pressure right now. That can be really exhausting.",
    "Stress can feel overwhelming, especially when many things pile up at once.",
    "I'm really glad you shared this. Stress can take a toll, and it's okay to acknowledge it.",
    "That sounds like a lot to handle. You're doing your best, even if it doesn't feel like it."
]

ANXIETY_RESPONSES = [
    "Anxiety can make the future feel uncertain and scary. You're not alone in feeling this way.",
    "It’s okay to feel anxious—many people struggle with these thoughts at times.",
    "When anxiety shows up, it can help to focus on what you can control right now.",
    "Your worries are valid, and it’s okay to take things one step at a time."
]

SADNESS_RESPONSES = [
    "I'm really sorry you're feeling this low. That can be very heavy to carry.",
    "Feeling low doesn’t mean you’re weak—it means you’re human.",
    "Some days are harder than others, and it’s okay to admit that today is one of them.",
    "You deserve care and understanding, especially when you’re feeling down."
]

GENERAL_SUPPORT_RESPONSES = [
    "Thank you for sharing this with me. I'm here to listen.",
    "You're not alone, and you don't have to go through this by yourself.",
    "It's okay to talk about how you're feeling. Your emotions matter.",
    "I'm really glad you reached out today."
]

FOLLOW_UP_QUESTIONS = [
    "Would you like to talk more about what's been causing this?",
    "Do you want to share what's been weighing on your mind?",
    "When did you start feeling this way?",
    "What usually helps you, even a little, when you feel like this?"
]

def get_local_response(user_message):
    msg = user_message.lower()

    if "stress" in msg or "overwhelm" in msg or "pressure" in msg:
        return random.choice(STRESS_RESPONSES) + " " + random.choice(FOLLOW_UP_QUESTIONS)

    if "anxious" in msg or "anxiety" in msg or "worried" in msg or "future" in msg:
        return random.choice(ANXIETY_RESPONSES) + " " + random.choice(FOLLOW_UP_QUESTIONS)

    if "sad" in msg or "low" in msg or "depressed" in msg or "lonely" in msg:
        return random.choice(SADNESS_RESPONSES) + " " + random.choice(FOLLOW_UP_QUESTIONS)

    return random.choice(GENERAL_SUPPORT_RESPONSES) + " " + random.choice(FOLLOW_UP_QUESTIONS)

@app.route("/", methods=["GET", "POST"])
def chat():
    global chat_history

    if request.method == "POST":
        user_message = request.form["message"]
        chat_history.append(("user", user_message))

        lower_msg = user_message.lower()

        # Crisis handling (always same safe message)
        if any(word in lower_msg for word in CRISIS_KEYWORDS):
            bot_reply = (
                "I'm really sorry you're feeling this way. You deserve care and support.\n\n"
                "If you are in immediate danger, please contact your local emergency services.\n\n"
                "📞 India: AASRA Helpline – 91-9820466726\n"
                "🌍 International: https://findahelpline.com\n\n"
                "If possible, please consider reaching out to someone you trust."
            )
        else:
            bot_reply = get_local_response(user_message)

        chat_history.append(("bot", bot_reply))

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
