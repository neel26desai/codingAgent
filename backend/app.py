from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import CodeAssistantAgent

# Initialize the agent
agent = CodeAssistantAgent()


app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

@app.route('/respond', methods=['POST'])
def respond():
    user_message = request.json.get('message')  # Capture the user message
    response = agent.process_input(user_message)
    response = response['chat_history'][-1].content
    return jsonify({"reply": response}) 

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5500)
