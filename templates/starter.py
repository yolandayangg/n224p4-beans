# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from pathlib import Path

# Open an Image
def image_data(path=Path("static/assets/"), img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            { 'file': "mountain_scenery.jpeg"}

        ]


    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # File to open
        file = path / img_dict['file']  # file with path for local access (backend)

        I1 = ImageDraw.Draw(file)
        I1.text((28, 36), "Amazing!", fill=(255, 0, 0)),

       img_show