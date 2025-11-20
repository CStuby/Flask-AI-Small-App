from flask import Flask, render_template, request
import json
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

with open("faq_data.json", "r", encoding="utf-8") as f:
    FAQ_DATA = json.load(f)


def build_prompt(user_question):
    faq_text = "\n".join(
        [f"Q: {item['question']}\nA: {item['answer']}" for item in FAQ_DATA]
    )

    prompt = f"""
You are a helpful FAQ assistant for Metropolia University of Applied Sciences.

You must answer ONLY using the information provided in the FAQ dataset below.
If the answer is not available in the dataset, reply:
"Sorry, I don't have information about that yet."

Here is the FAQ dataset:

{faq_text}

User question: {user_question}

Your answer:
"""
    return prompt


@app.route("/", methods=["GET", "POST"])
def index():
    answer = None

    if request.method == "POST":
        user_question = request.form["question"]

        prompt = build_prompt(user_question)

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        answer = response.text

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
