import os, io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mid_test_django.settings')

import django
django.setup()

from test_web.models import *
from google.cloud import vision
client = vision.ImageAnnotatorClient()


def get_area(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = min(x1, x2, x3, x4)
    a2 = max(x1, x2, x3, x4)
    b1 = min(y1, y2, y3, y4)
    b2 = max(y1, y2, y3, y4)
    return abs(a1-a2) * abs(b1-b2)


def get_name(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    area = 0
    cur_area = 0
    index = 0

    for i, text in enumerate(texts):
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        if i > 0:
            cur_area = get_area(int(vertices[0][1:-1].split(",")[0]), int(vertices[0][1:-1].split(",")[1]),
                                int(vertices[1][1:-1].split(",")[0]), int(vertices[1][1:-1].split(",")[1]),
                                int(vertices[2][1:-1].split(",")[0]), int(vertices[2][1:-1].split(",")[1]),
                                int(vertices[3][1:-1].split(",")[0]), int(vertices[3][1:-1].split(",")[1]))
        if area < cur_area:
            area = cur_area
            index = i

    import re
    na = texts[index].description
    regex = r"\s" + re.escape(na) + r".*\s"
    name = re.search(regex, texts[0].description).group(0).strip().replace("\n", " ")
    return name
#print(name)
#print(texts[index].description+texts[index+1].description)


def get_text(img):
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description
def save():
    csv_path = 'medicine4.csv'
    with open(csv_path, encoding = 'UTF8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
        #print(row['\ufeffid'])
            Drug.objects.create(

                id = row['\ufeffid'], name = row['제품명'], company = row['제품회사'],
                ingredient = row['성분'], effect = row['효능'], use = row['용법']
            )
