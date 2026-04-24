from flask import Flask, request, render_template
import random

app = Flask(__name__)

def generate_questions(topic):
    return f"""
    Topic: {topic}

    Multiple Choice Questions:
    1. What is {topic}?
       a) Option A
       b) Option B
       c) Option C
       d) Option D
       Answer: a

    2. Basic concept of {topic}?
       a) A
       b) B
       c) C
       d) D
       Answer: b

    Short Answer:
    1. Explain {topic}
    2. Importance of {topic}

    Long Answer:
    1. Describe {topic} in detail
    """

@app.route("/", methods=["GET", "POST"])
def home():
    questions = ""

    if request.method == "POST":
        topic = request.form["topic"]
        questions = generate_questions(topic)

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)