from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # This allows all origins to access your API

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    return "Word not found."

@app.route("/search", methods=["GET"])
def search():
    word = request.args.get("word")
    meaning = get_meaning(word)
    return jsonify({"word": word, "meaning": meaning})

if __name__ == "__main__":
    app.run(debug=True)
