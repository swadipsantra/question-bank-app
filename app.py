from flask import Flask, request, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_questions(topic):
    prompt = f"""
    Generate a question bank for: {topic}

    Include:
    - 5 MCQs (with answers)
    - 3 Short questions (with answers)
    - 2 Long questions (with answers)

    Keep answers clear and simple.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # ✅ lightweight + cheap
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

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