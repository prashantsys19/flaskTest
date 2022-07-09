
from flask import Flask, jsonify, request

app = Flask(__name__)

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
    app.run(host="0.0.0.0", port=5000)
