from flask import Flask, render_template, request

from genai_manager import GenaiManager

app = Flask(__name__)
ai = GenaiManager()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
    response = ai.chat(query)
    return response


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=54321)