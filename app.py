#!flask/bin/python
from flask import Flask, request, abort, jsonify
import parser

app = Flask(__name__)

base_url = '/api/v1.0'

def responsify(output):
    return jsonify({ "response" : output })

@app.route(base_url+"/request", methods=['POST'])
def index():
    if not request.json or not 'request' in request.json:
        abort(400)
    sentence = request.json['request']
    parsed = parser.parse_request(sentence)
    return responsify(parsed)


if __name__ == "__main__":
    app.run()
