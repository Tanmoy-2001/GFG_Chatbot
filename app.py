from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = respond(user_message)
    return jsonify({'bot_response': bot_response})

def respond(user_message):
    # Your chatbot logic here
    if user_message.lower() == 'hello':
        return "Hi there!"
    elif user_message.lower() == 'how are you?':
        return "I'm just a bot, but thanks for asking!"
    else:
        return "I didn't quite understand that."

if __name__ == '__main__':
    app.run(debug=True)
