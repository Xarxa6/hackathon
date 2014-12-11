from flask import Flask, request, abort, jsonify
import parser
import dal
import log

app = Flask(__name__)

base_url = '/api/v1.0'

responsify = lambda output: jsonify({ "response" : output })

@app.route(base_url+"/request", methods=['POST'])
def index():
    if not request.json or not 'request' in request.json:
        abort(400)
    sentence = request.json['request']
    tags = parser.parse_request(sentence)
    analyses = dal.query_analyses(tags)
    return responsify(analyses)
