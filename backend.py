from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_question', methods=['POST'])
def generate_question():
    topic = request.json.get('topic')
    # Call the AI model to generate the question
    question = generate_physics_question(topic)
    return jsonify({'question': question})

def generate_physics_question(topic):
    # AI model integration here
    return "Sample question related to " + topic

if __name__ == '__main__':
    app.run(debug=True)
