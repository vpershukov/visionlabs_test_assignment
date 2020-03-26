#! /usr/bin/env python
from flask import Flask, json, jsonify
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"key": "value"})


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return jsonify({"User": username})


@app.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return jsonify({"post" : post_id})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='port')
    parser.add_argument('--port', dest='port', action='store', type=int, help='using port for mock', default=6000)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True, threaded=True)
