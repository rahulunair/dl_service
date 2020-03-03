#!/usr/bin/env python
import base64
import sys
import random
import string
from io import BytesIO
from PIL import Image

from main import classify

def read_buffer():
    """read encoded image save it local and return path."""
    b64_encoded = sys.stdin.buffer.read()
    decoded_img = base64.urlsafe_b64decode(b64_encoded) 
    img_buffer = BytesIO()
    img_buffer.write(decoded_img)
    img_buffer.seek(0)
    image = Image.open(img_buffer).convert("RGB")
    input_img_path = "input_img_%s.jpg" % rand_string()
    image.save(input_img_path)
    return input_img_path

def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if line=="":
            break
    return buf

def rand_string():
    rand_str = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    return rand_str

if __name__ == "__main__":
    #b64_img = read_buffer()
    print("inside main block of handler.py")
    b64_img = get_stdin()
    print(classify(b64_img))
