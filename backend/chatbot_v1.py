from flask import Flask, request, jsonify
from backend.chatbot_v1 import chatbot

app = Flask(__name__)
english_bot = chatbot()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')
    response = english_bot.get_response(question)
    return jsonify({'response': str(response)})

if __name__ == '__main__':
    app.run(debug=True)
