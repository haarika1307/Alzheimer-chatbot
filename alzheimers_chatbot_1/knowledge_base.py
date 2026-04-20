KNOWLEDGE_BASE = {
    "alzheimer": {
        "keywords": ["alzheimer", "alzheimers", "ad"],
        "response": (
            "Alzheimer’s disease is a progressive condition that affects memory, "
            "thinking, and daily functioning. It usually develops gradually over time.\n\n"
            "Only a qualified healthcare professional can diagnose Alzheimer’s disease."
        )
    },

    "mci": {
        "keywords": ["mci", "mild cognitive impairment"],
        "response": (
            "Mild Cognitive Impairment (MCI) involves noticeable changes in memory or "
            "thinking that are greater than expected for age, but do not severely "
            "impact daily independence."
        )
    },

    "normal_aging": {
        "keywords": ["normal aging", "forgetfulness", "age-related"],
        "response": (
            "Occasional forgetfulness can be a normal part of aging. Persistent or "
            "worsening memory issues should be discussed with a doctor."
        )
    },

    "cure": {
        "keywords": ["cure", "treatment", "medication"],
        "response": (
            "There is currently no cure for Alzheimer’s disease. However, medical care, "
            "lifestyle support, and early planning can help manage symptoms."
        )
    },

    "doctor": {
        "keywords": ["doctor", "see a doctor", "consult"],
        "response": (
            "A doctor can perform proper cognitive assessments, review medical history, "
            "and suggest appropriate next steps."
        )
    }
}


def get_knowledge_response(user_message):
    msg = user_message.lower()

    for entry in KNOWLEDGE_BASE.values():
        for keyword in entry["keywords"]:
            if keyword in msg:
                return (
                    entry["response"]
                    + "\n\n"
                    "If this concerns you personally, consulting a healthcare professional is recommended."
                )

    return (
        "I can share general information, but a healthcare professional is best suited "
        "for personal medical advice."
    )
