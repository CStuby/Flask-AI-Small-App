# Flask-AI-Small-App

A lightweight Flask web application that uses AI to answer common questions about Metropolia services. 
The app helps users get quick answers from a curated FAQ dataset by using Google Gemini 2.5 Flash to interpret the question and match it to known answers.
If the answer isn’t available, the assistant politely responds that it doesn't have the available information.

## 🚀 Features

- ✔ AI-powered FAQ assistant
- ✔ Uses Gemini 2.5 Flash for natural language understanding
- ✔ Prevents hallucinations using a controlled prompt
- ✔ Flask backend
- ✔ Simple HTML frontend
- ✔ Easy to extend with more FAQs

## 🎯 Problem This Solves

Students may find information about:
- Course enrollment  
- Password resets  
- Schedules  
- IT services  

These answers can be scattered across various platforms.  
This assistant centralizes the info and uses AI to respond in a user-friendly way.

## 📁 Project Structure

```
Flask Small Coding App/
│
├── app.py
├── faq_data.json
├── requirements.txt
│
└── templates/
    └── index.html
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CStuby/Flask-AI-Small-App.git
   cd Flask-AI-Small-App-main
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Get your API key**:
   ```bash
   Get one at: https://aistudio.google.com/app/api-keys
   ```
4. **Set your API key (Windows)**: 
   ```bash
   setx GOOGLE_API_KEY "your_api_key_here"
   ```
5. **Run the app**:
   ```bash
   python app.py
   ```
6. **Open your browser at**:
   ```
   http://127.0.0.1:5000
   ```
## 🧠 How It Works

1. User enters a question

2. Flask composes a prompt containing:

    - the FAQ dataset

    - the user’s question

    - strict instructions

3. Gemini processes the input

4. If the answer exists, Gemini returns the matching FAQ

5. If not, it responds with:
    "Sorry, I don't have information about that yet."

6. The UI displays the result

## 🛠️ Tech Stack

- Python
- Flask
- HTML / Jinja2 templates
- Google Gemini API (genai)
- JSON dataset

## 📜 License

This project is for educational and demonstration purposes.
Feel free to modify it.
