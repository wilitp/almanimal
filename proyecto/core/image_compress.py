from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def compress(image):

    im = Image.open(image)

    output = BytesIO()

    original_width, original_height = im.size
    aspect_ratio = round(original_width / original_height)
    new_height = 1500
    new_width = new_height * aspect_ratio


    im = im.resize((new_width, new_height))

    im.save(output, format='JPEG', quality=90)
    output.seek(0)

    image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

    return image