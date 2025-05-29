from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    prompt = f"""السؤال: {question}
اشرح الإجابة بشكل مبسط وواضح، وحدد موقعها إن أمكن داخل كتاب العلوم للصف السادس."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

@app.route("/", methods=["GET"])
def index():
    return "خادم مساعد الذكاء الاصطناعي يعمل ✅"

if __name__ == "__main__":
    app.run()
