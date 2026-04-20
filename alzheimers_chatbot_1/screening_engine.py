import random

user_data = {}

QUESTIONS = [
    "Do you often forget recent conversations?",
    "Do you find daily tasks harder than before?",
    "Do you misplace items more frequently?",
    "Do you feel confused about dates or events?"
]

WORDS = ["apple", "table", "penny", "river", "chair", "clock"]


# ---------- RESULT TEXTS (IMPROVED WORDING) ----------

NORMAL_RESULT_TEXT = (
    "Screening Summary\n\n"
    "Your responses fall within a range that is generally considered normal.\n\n"
    "Occasional forgetfulness can happen for many reasons, including stress, fatigue, "
    "or normal aging. At this stage, there are no strong signs suggesting significant "
    "cognitive difficulty.\n\n"
    "If you notice any new or persistent changes in memory or thinking in the future, "
    "discussing them with a healthcare professional can be helpful.\n\n"
    "This screening is for awareness only and is not a medical diagnosis."
)

MILD_CONCERN_RESULT_TEXT = (
    "Screening Summary\n\n"
    "Your responses suggest some mild changes in memory or thinking that may be worth "
    "paying attention to.\n\n"
    "This does not mean that you have a medical condition. Factors such as stress, sleep, "
    "mood, or temporary health issues can also affect memory.\n\n"
    "If these concerns continue, worsen, or interfere with daily activities, it may be "
    "helpful to consult a qualified healthcare professional for a more detailed evaluation.\n\n"
    "This screening is for awareness only and does not provide a medical diagnosis."
)

FURTHER_EVALUATION_RESULT_TEXT = (
    "Screening Summary\n\n"
    "Your responses indicate changes that may benefit from further professional evaluation.\n\n"
    "This screening tool cannot determine the cause of these changes. A healthcare "
    "professional can perform detailed assessments, review medical history, and provide "
    "appropriate guidance.\n\n"
    "If possible, consider discussing these concerns with a doctor. Bringing a family "
    "member or caregiver to the appointment may also be helpful.\n\n"
    "This screening is for awareness only and is not a medical diagnosis."
)


# ---------- HELPER FUNCTION ----------

def is_screening_active(user_id):
    return user_id in user_data


# ---------- CORE SCREENING LOGIC ----------

def process_user_message(user_id, message):
    msg = message.lower().strip()

    if user_id not in user_data:
        user_data[user_id] = {
            "state": "START",
            "q": 0,
            "answers": [],
            "recall_words": []
        }

    u = user_data[user_id]

    # START
    if u["state"] == "START":
        u["state"] = "CONSENT"
        return (
            "Hello. This is a short cognitive screening tool.\n"
            "It is intended for awareness only and does not provide a medical diagnosis.\n\n"
            "Do you consent to continue? (yes/no)"
        )

    # CONSENT
    if u["state"] == "CONSENT":
        if msg == "yes":
            u["state"] = "Q"
            return QUESTIONS[0]
        return "Screening ended. You may return anytime if you wish to continue."

    # QUESTIONS
    if u["state"] == "Q":
        u["answers"].append(msg)
        u["q"] += 1

        if u["q"] < len(QUESTIONS):
            return QUESTIONS[u["q"]]

        u["recall_words"] = random.sample(WORDS, 3)
        u["state"] = "SHOW"
        return (
            "Please remember the following three words:\n"
            f"{', '.join(u['recall_words'])}\n\n"
            "I will ask you to recall them shortly."
        )

    # SHOW WORDS
    if u["state"] == "SHOW":
        u["state"] = "ASK"
        return "Please type the three words you remember."

    # FINAL STEP + RESULT
    if u["state"] == "ASK":
        score = sum(1 for a in u["answers"] if a != "no")

        u["state"] = "END"

        if score <= 2:
            return NORMAL_RESULT_TEXT
        elif score <= 4:
            return MILD_CONCERN_RESULT_TEXT
        else:
            return FURTHER_EVALUATION_RESULT_TEXT

    return "Session completed. If you have questions, feel free to ask."
