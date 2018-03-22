from flask import Flask
from flask import request
import os
import socket
import subprocess
from subprocess import CalledProcessError
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    f = request.files['data']
    filename = secure_filename(f.filename)
    f.save(filename)
    #result = subprocess.check_output(["ls", "-al"])
    try:
        result = subprocess.check_output(["python", "./classify_nsfw.py", "--model_def", "nsfw_model/deploy.prototxt", "--pretrained_model", "nsfw_model/resnet_50_1by2_nsfw.caffemodel", filename])
        os.remove(filename)
    except CalledProcessError as e:
        result = e.output

    result = result.split(" ")[-1]
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, processes=4)
