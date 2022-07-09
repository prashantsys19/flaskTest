
from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def index():
    return "Hello world"

@app.route('/sum', methods = ['Post'])
def addTwoNum():
    dataDic = request.get_json()
    x=dataDic['x']
    y=dataDic['y']
    z = x+y
    retJson = {
        "z":z
    }    
    return jsonify(retJson)

if __name__ == "__main__":
    app.run()
