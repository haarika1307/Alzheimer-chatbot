HELPLINES = {
    "Alzheimer’s Support (India)": "1800-599-0019",
    "Mental Health Helpline (India)": "9152987821",
    "Emergency Services": "112"
}

def get_helpline_message():
    message = "If you feel you need immediate support, you may contact:\n"
    for name, number in HELPLINES.items():
        message += f"- {name}: {number}\n"
    return message
