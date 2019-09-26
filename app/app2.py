#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)


class App(Resource):
    def get(self):
        return jsonify({'app': 'app2'})
    def post(self, text):
        return jsonify({
            'app' : 'app2',
            'text' : text
        })


api.add_resource(App, '/start/app')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)