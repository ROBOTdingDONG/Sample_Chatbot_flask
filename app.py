from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = "Hello!"
    if request.method == "POST":
        user_input = request.form.get("user_input")
        # Placeholder for testing; replace with OpenAI API call later
        response_text = f"Echo: {user_input}"
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
