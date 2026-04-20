NORMAL_TIPS = [
    "Maintain a regular daily routine.",
    "Stay socially active and engage in conversations.",
    "Get adequate sleep and regular physical activity.",
    "Challenge your brain with reading, puzzles, or learning new skills."
]

MILD_CONCERN_TIPS = [
    "Keep a simple memory or activity journal.",
    "Reduce stress and avoid multitasking when possible.",
    "Discuss any concerns with a trusted family member.",
    "Consider scheduling a routine check-up with a healthcare professional."
]

GENERAL_NEXT_STEPS = [
    "If concerns persist, consider seeking a professional evaluation.",
    "Bring a family member or caregiver when visiting a doctor.",
    "Early consultation can help clarify concerns and plan next steps."
]

def get_general_tips():
    message = "Here are some general steps you may find helpful:\n"
    for tip in NORMAL_TIPS:
        message += f"- {tip}\n"
    return message


def get_seeking_help_guidance():
    message = "Here are some suggested next steps:\n"
    for step in GENERAL_NEXT_STEPS:
        message += f"- {step}\n"
    return message
