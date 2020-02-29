#!usr/bin/env python
#
# Copyright (c) 2019 Intel Corporation
#
# Main author:
#   * unrahul <rahul.unnikrishnan.nair@intelcom>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""a rest api for image recognition"""
#
#
#
import io


from PIL import Image
import flask
from flask import Flask
from flask_cors import CORS
from main import classify

app = Flask(__name__)
CORS(app)


banner = {
    "what": "image recognition api",
    "usage": {
        "client": "curl -i  -X POST -F img=@data/cat.jpg 'http://localhost:5000/recog'",
        "server": "docker run -d -p 5000:5000 stacks_img_recog",
    },
}


@app.route("/usage", methods=["GET"])
def usage():
    return flask.jsonify({"info": banner}), 201


@app.route("/recog", methods=["POST"])
def recog():
    if flask.request.files.get("img"):
        img = flask.request.files["img"].read()
        img = Image.frombytes("RGBA", (128,128), img, "raw")
        y_hat = classify(img)
        return flask.jsonify({"class": y_hat[0], "prob": y_hat[1]}), 201
    return flask.jsonify({"status": "not an image file"})


@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5059)
