from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

generator = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def home():
    questions = ""

    if request.method == "POST":
        topic = request.form["topic"]

        prompt = f"""
        Create a structured question bank on the topic: {topic}

        1. 5 Multiple Choice Questions with 4 options and correct answer
        2. 3 Short Answer Questions
        3. 2 Long Answer Questions

        Format clearly.
        """

        result = generator(prompt, max_length=300, num_return_sequences=1)
        questions = result[0]['generated_text']

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)