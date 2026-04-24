from flask import Flask, request, render_template
import random

app = Flask(__name__)

def generate_questions(topic):
    mcq_templates = [
        f"What is {topic}?",
        f"Which best describes {topic}?",
        f"What is the main purpose of {topic}?",
        f"{topic} is related to which field?",
        f"Which of the following is a feature of {topic}?"
    ]

    short_templates = [
        f"Define {topic}.",
        f"Explain the importance of {topic}.",
        f"List applications of {topic}.",
        f"Write a short note on {topic}.",
        f"Why is {topic} useful?"
    ]

    long_templates = [
        f"Explain {topic} in detail with examples.",
        f"Discuss advantages and disadvantages of {topic}.",
        f"Describe the working process of {topic}.",
        f"Write a detailed explanation of {topic}."
    ]

    random.shuffle(mcq_templates)
    random.shuffle(short_templates)
    random.shuffle(long_templates)

    output = f"📘 Topic: {topic}\n\n"

    # MCQ
    output += "SECTION A: Multiple Choice Questions\n"
    for i, q in enumerate(mcq_templates[:5], 1):
        output += f"{i}. {q}\n"
        output += "   a) Option A\n   b) Option B\n   c) Option C\n   d) Option D\n   Answer: a\n\n"

    # Short
    output += "SECTION B: Short Answer Questions\n"
    for i, q in enumerate(short_templates[:3], 1):
        output += f"{i}. {q}\n"
    output += "\n"

    # Long
    output += "SECTION C: Long Answer Questions\n"
    for i, q in enumerate(long_templates[:2], 1):
        output += f"{i}. {q}\n"

    return output


@app.route("/", methods=["GET", "POST"])
def home():
    questions = ""

    if request.method == "POST":
        topic = request.form["topic"]
        questions = generate_questions(topic)

    return render_template("index.html", questions=questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)