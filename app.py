from flask import Flask, render_template, request
import os
import openai  # Ensure you've installed the openai package with pip install openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = "Hello!"
    if request.method == "POST":
        user_input = request.form.get("user_input")
        # Call the OpenAI API with the user input (placeholder for now)
        # Example: 
        # openai_response = openai.Completion.create(
        #     engine="text-davinci-003",
        #     prompt=user_input,
        #     max_tokens=50
        # )
        # response_text = openai_response.choices[0].text.strip()
        response_text = f"Echo: {user_input}"  # Temporary echo for testing
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
