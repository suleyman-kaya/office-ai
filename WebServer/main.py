from flask import Flask, request
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    return data

app.run()
