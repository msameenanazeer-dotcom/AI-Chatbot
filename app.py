from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "name" in message:
        return "I am a simple AI chatbot."
    elif "python" in message:
        return "Python is a popular programming language used in AI."
    elif "ai" in message:
        return "AI means Artificial Intelligence."
    elif "bye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    return jsonify({"response": chatbot(message)})

if __name__ == "__main__":
    app.run(debug=True)
