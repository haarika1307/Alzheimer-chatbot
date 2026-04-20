from flask import Flask, render_template, request, jsonify

from intent_detector import detect_intent
from helplines import get_helpline_message
from tips import get_general_tips, get_seeking_help_guidance
from screening_engine import process_user_message, is_screening_active
from knowledge_base import get_knowledge_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    user_id = "demo_user"

    screening_active = is_screening_active(user_id)

    intent = detect_intent(user_message)
    print("Detected intent:", intent, "| Screening active:", screening_active)

    # 🚨 ALWAYS PRIORITY: SAFETY
    if intent == "emotional_distress":
        reply = (
            "I’m really sorry you’re feeling this way.\n\n"
            + get_helpline_message()
        )

    # 🧠 SCREENING HAS PRIORITY OVER ALL EXCEPT DISTRESS
    elif screening_active:
        reply = process_user_message(user_id, user_message)

    # 📚 MEDICAL EDUCATION (GENERAL ONLY)
    elif intent == "medical_information":
        reply = get_knowledge_response(user_message)

    # 🧭 GUIDANCE / NEXT STEPS
    elif intent == "seeking_help":
        reply = (
            "I understand your concern.\n\n"
            + get_general_tips()
            + "\n"
            + get_seeking_help_guidance()
        )

    # 🛠 TECH SUPPORT
    elif intent == "technical_issue":
        reply = (
            "Thanks for letting me know. Could you describe "
            "the issue you’re facing with the chatbot?"
        )

    # 🧩 DEFAULT → START SCREENING
    else:
        reply = process_user_message(user_id, user_message)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
