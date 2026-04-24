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
            model="command-light",   # lightweight model
            prompt=prompt,
            max_tokens=400,
            temperature=0.7
        )
        return response.generations[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"