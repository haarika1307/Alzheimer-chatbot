from transformers import pipeline

# Load model (first time takes time)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

INTENT_LABELS = [
    "seeking_help",
    "emotional_distress",
    "medical_information",
    "technical_issue",
    "general_chat"
]

def detect_intent(text):
    result = classifier(text, INTENT_LABELS)
    return result["labels"][0]


# Test manually
if __name__ == "__main__":
    test_texts = [
        "I am worried about my memory",
        "The chatbot is not working",
        "Hello there",
        "I feel scared and confused"
    ]

    for text in test_texts:
        intent = detect_intent(text)
        print(f"Text: {text}")
        print(f"Detected intent: {intent}\n")
