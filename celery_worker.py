
import os, glob
from PIL import Image
from celery import Celery

app = Celery('celery_worker', broker='pyamqp://guest@localhost//')


@app.task
def task1(image_pass):
    height = 512
    width = 512
    for infile in glob.glob(image_pass):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            new_img = im.resize((height, width), Image.ANTIALIAS)
            im.mode = 'RGB'
            new_img.save(file + "_MINI.jpeg", "JPEG")

    return 'Successfully'

