from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from poem_generator import PoemGenerator
import json

app = Flask(__name__)
cors = CORS(app)

generator = PoemGenerator()

@app.after_request
def atHeaders(response):
        response.headers['Access-Control-Allow-Origin'] = "*"
        response.headers["Access-Control-Allow-Credentials"] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, access-control-allow-headers'
        return response

@app.route("/api/poem", methods=['GET'])
@cross_origin()
def poem():
        # res = generator.generate_poem()
        # print(json.dumps(res))
        return jsonify({
                "poem" : 1,
        })

if __name__ == '__main__':
	app.run(debug=True)