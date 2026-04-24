from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}


def generate_questions(topic):
    prompt = f"""
    Generate a question bank on the topic: {topic}

    Include:
    - 5 MCQs with answers
    - 3 short questions with answers
    - 2 long questions with answers
    """

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        result = response.json()

        return result[0]["generated_text"]

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():
    questions = ""

    if request.method == "POST":
        topic = request.form["topic"]
        questions = generate_questions(topic)

    return render_template("index.html", questions=questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)