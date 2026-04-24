from flask import Flask, request, render_template

app = Flask(__name__)

def generate_questions(topic):
    return f"""
📘 Topic: {topic}

SECTION A: Multiple Choice Questions
1. What is {topic}?
   a) A concept
   b) A tool
   c) A process
   d) A system
   Answer: a

2. Purpose of {topic}?
   a) Analysis
   b) Storage
   c) Display
   d) None
   Answer: a

3. {topic} is used in:
   a) Data Science
   b) Cooking
   c) Gaming
   d) Driving
   Answer: a

4. One advantage of {topic}:
   a) Better decision making
   b) Slower performance
   c) Less usage
   d) None
   Answer: a

5. {topic} helps in:
   a) Pattern recognition
   b) Sleeping
   c) Driving
   d) Gaming
   Answer: a


SECTION B: Short Answer Questions
1. Define {topic}.
2. Explain the importance of {topic}.
3. List applications of {topic}.


SECTION C: Long Answer Questions
1. Explain {topic} in detail with examples.
2. Discuss advantages and disadvantages of {topic}.
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