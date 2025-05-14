from flask import Flask, request, jsonify
from flashcard_generator import generate_flashcards

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    flashcards = generate_flashcards(text)
    return jsonify({"flashcards": flashcards})

if __name__ == "__main__":
    app.run(debug=True)
