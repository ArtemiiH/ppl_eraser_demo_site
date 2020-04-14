import base64
from io import BytesIO
from PIL import Image


def prepare_image_for_json(file, size=(512, 512)):
    image = Image.open(file)
    image.thumbnail(size)
    imageIO = BytesIO()
    image.save(imageIO, "PNG")
    imageIO.seek(0)
    return base64.b64encode(imageIO.read()).decode('utf-8')
