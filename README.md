# Flask-AI-Small-App

A lightweight Flask web application that uses AI to answer common questions about Metropolia services. 
The app helps users get quick answers from a curated FAQ dataset by using Google Gemini 2.5 Flash to interpret the question and match it to known answers.
If the answer isn’t available, the assistant responds politely and safely.

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

These answers are scattered across various platforms.  
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

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CStuby/Flask-AI-Small-App.git
   cd prototype-linkedin-future
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your API key (Windows)**: 
   ```bash
   setx OPENAI_API_KEY "your_api_key_here"
   ```
4. **Run the app**:
   ```bash
   python app.py
   ```
5. **Open your browser at**:
   ```
   http://127.0.0.1:5000
   ```
## 🧠 How It Works

1. User enters a question

2. Flask sends the question plus the FAQ dataset to Gemini

3. Prompt engineering ensures the model:

    - Answers only from the dataset

    - Responds with a fallback message otherwise

4. The model returns the best answer

5. The UI displays it instantly

## 🛠️ Tech Stack

- Python
- Flask
- HTML / Jinja2 templates
- OpenAI-compatible LLM API

## 📜 License

This project is for educational and demonstration purposes.
Feel free to modify it.
