# 🧠 Alzheimer’s & MCI Screening Chatbot

An AI-powered, safety-focused chatbot designed to support **early awareness of cognitive changes** related to Alzheimer’s disease and Mild Cognitive Impairment (MCI) through natural conversation and simple screening tasks.

> ⚠️ This tool is for awareness and guidance only.  
> It does **not** provide medical diagnosis or treatment.

---

## 📌 Problem Statement

Early stages of Alzheimer’s disease and MCI often present as subtle changes in memory, thinking, and daily functioning. Many individuals may not recognize these early signs, and access to professional cognitive screening may be limited.

There is a need for an **accessible, user-friendly tool** that can:
- Encourage early awareness
- Provide general educational information
- Guide users toward appropriate next steps
- Maintain safety and ethical boundaries

---

## 🎯 Project Objective

The goal of this project is to build a **responsible AI chatbot** that:

- Conducts **basic, non-diagnostic cognitive screening**
- Provides **educational information** about Alzheimer’s disease and MCI
- Detects **emotional distress** and escalates support appropriately
- Encourages **professional medical consultation** when needed
- Maintains user safety, privacy, and ethical AI principles

---

## 🧩 Key Features

### 🧪 Cognitive Screening
- Consent-based screening flow
- Memory-related questions
- Simple recall tasks
- Non-diagnostic result summaries:
  - Normal
  - Mild Concern
  - Needs Further Evaluation

### 📚 Medical Education (Safe & Non-Personalized)
- General information about:
  - Alzheimer’s disease
  - Mild Cognitive Impairment (MCI)
  - Normal aging vs concerning changes
- Clear disclaimers and doctor-visit guidance

### 🚨 Safety & Ethics
- Emotional distress detection
- Automatic helpline escalation
- Supportive and empathetic language
- No medical diagnosis or treatment advice

### 🤖 Agentic AI Design
- Intent-based routing (Help, Information, Screening, Distress)
- State-aware conversation handling
- Priority-based decision logic

### 🎨 User Interface
- Clean chat interface
- User and bot message separation
- Typing indicator
- Input locking during bot response
- Accessible and simple design

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – backend web framework
- **Hugging Face Transformers**
  - `facebook/bart-large-mnli` for intent detection
- **HTML, CSS, JavaScript** – frontend UI
- **Git & GitHub** – version control and collaboration

---

## 🧠 System Architecture (High-Level)

1. User sends a message via the chat UI
2. Intent detection determines message type:
   - Screening
   - Medical information
   - Seeking help
   - Emotional distress
3. Priority rules decide response flow:
   - Distress → Helplines
   - Active screening → Screening engine
   - Medical questions → Knowledge module
   - Guidance → Tips module
4. Response is safely returned to the user

---

## ⚠️ Ethical Considerations

- This chatbot **does not diagnose** Alzheimer’s or MCI
- All medical information is **educational only**
- Users are encouraged to consult qualified healthcare professionals
- Emotional distress is handled with immediate support resources
- Designed with **responsible AI principles** in mind

---


