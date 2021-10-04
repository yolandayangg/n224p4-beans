from PIL import Image, ImageDraw
import numpy
import base64
from io import BytesIO
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f



# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)

def image_base64_MSG(img, img_type):
    d1=ImageDraw.Draw(img)
    d1.text((10,10), "Amazing!", fill="white")
    img.show()
    return "data:image/" + img_type + ";base64," +image_base64(img, img_type)

# color_data prepares a series of images for data analysis
def image_data(path=Path("static/assets/"), images=None):  # path of static images is defaulted
    if images is None:  # color_dict is defined with defaults

        images = [
            {'source': "Sergei Akulich", 'label': "Pristine Forest", 'file': "forestttt.jpeg"},
            {'source': "Carlsbad", 'label': "Carlsbad Flower Fields", 'file': "flowers.jpeg" }
        ]


# gather analysis data and meta data for each image, adding attributes to each row in table
    for image in images:
        filename = path / image['file']  # file with path for local access (backend)

        img_object = Image.open(filename)




        # Python Image Library operations
        img_reference = Image.open(filename)  # PIL
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        image['format'] = img_reference.format
        image['mode'] = img_reference.mode
        image['size'] = img_reference.size



        # Conversion of original Image to Base64, a string format that serves HTML nicely
        image['base64'] = image_formatter(img_reference, image['format'])
        # Numpy is used to allow easy access to data of image, python list
        img_data = img_object.getdata()
        image['data'] = numpy.array(img_data)
        image['hex_array'] = []
        image['binary_array'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in image['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            image['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            image['binary_array'].append(bin_value)
        # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        image['gray_data'] = []
        for pixel in image['data']:
            average = (int(pixel[0]) + pixel[1] + pixel[2]) // 3  # integer division
            if len(pixel) > 3:
                image['gray_data'].append((average, average, average, pixel[3]))
            else:
                image['gray_data'].append((average, average, average))
        img_reference.putdata(image['gray_data'])
        image['base64_GRAY'] = image_formatter(img_reference, image['format'])
    return images  # list is returned with all the attributes for each image dictionary


# run this as standalone tester to see data printed in terminal
if __name__ == "__main__":
    local_path = Path("/static/assets/")
    img_test = [
        {'source': "Sergei Akulich", 'label': "Pristine Forest", 'file': "forestttt.jpeg"},
        {'source': "Carlsbad", 'label': "Carlsbad Flower Fields", 'file': "flowers.jpeg"}
    ]

    images = image_data(local_path, img_test)  # path of local run
    for image in images:
        # print some details about the image so you can validate that it looks like it is working
        # meta data
        print("---- meta1 data -----")
        print(image['label'])
        print(image['format'])
        print(image['mode'])
        print(image['size'])
        # data
        print("----  data  -----")
        print(image['data'])
        print("----  gray data  -----")
        print(image['gray_data'])
        print("----  hex of data  -----")
        print(image['hex_array'])
        print("----  bin of data  -----")
        print(image['binary_array'])
        # base65
        print("----  base64  -----")
        print(image['base64'])

        filename = local_path / image['file']




print()


