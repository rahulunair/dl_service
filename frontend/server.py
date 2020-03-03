#!/usr/bin/env python
"""server basic templates to upload a file to be sent to the classifier"""
import ast
import base64
import os

import numpy as np
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            print("No file part")
            return redirect(request.url)
        img_file = request.files["file"]
        if img_file.filename == "":
            print("No selected file")
            return redirect(request.url)
        if img_file:
            filename = img_file.filename
            img_file.save(os.path.join("static", filename))

            result = classifier(img_file.filename)
            path_to_image = url_for("static", filename=filename)
            res_args = {"output": result, "path_to_image": path_to_image, "size": 224}
            return render_template("show.html", result=res_args)
    return render_template("index.html")

def classifier(img):
    """send img file to classifier and get the output."""
    img = open(os.path.join("static", img), "rb").read()
    data = {"img" : img}
    #resp = requests.post("http://127.0.0.1:8080/function/img-recog-faas", files=data)
    resp = requests.post("http://localhost:5059/recog", files=data)
    cls = ast.literal_eval(resp.content.decode("utf-8"))["class"]
    return cls 
    #return resp.content





if __name__ == "__main__":
    app.run(debug=True)
