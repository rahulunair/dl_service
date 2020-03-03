#!/usr/bin/env python
import base64
import sys
import random
import string
from io import BytesIO
from PIL import Image

from main import classify

def img_buffer():
    input_buff = sys.stdin.buffer.read()
    decoded_img = base64.urlsafe_b64decode(input_buff) 
    img_bytes = BytesIO(input_buff)
    image = Image.open(img_bytes).convert("RGB")
    input_img_path = "input_img_%s.jpg" % rand_string()
    image.save(input_img_path)
    return input_img_path

def rand_string():
    rand_str = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    return rand_str

if __name__ == "__main__":
    classify(img_buffer())
