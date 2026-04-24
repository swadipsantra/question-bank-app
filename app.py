from flask import Flask, request, render_template
import cohere
import os

app = Flask(__name__)

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_questions(topic):
    prompt = f"""
    Create a question bank for: {topic}

    Include:
    - 5 MCQs with answers
    - 3 short questions with answers
    - 2 long questions with answers
    """

    try:
        response = co.generate(
            model="command-light",
            prompt=prompt,
            max_tokens=400,
            temperature=0.7
        )
        return response.generations[0].text.strip()

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