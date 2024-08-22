from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def responseToTheHomeRoute():
    return jsonify("Added home route.")

if __name__ == '__main__':
    app.run()