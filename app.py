from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify("Welcome to the AI Builders Hub!")

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"id": 1, "name": "Sample Data"}
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
