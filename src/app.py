from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return {'message': 'Hello, World!'}, 200

def serve():
    app.run(debug=True, host='0.0.0.0', port=5001)
