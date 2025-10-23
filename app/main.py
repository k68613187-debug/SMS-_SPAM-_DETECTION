from flask import Flask, request, jsonify
from src.predict import predict_message

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')
    prediction = predict_message(message)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
