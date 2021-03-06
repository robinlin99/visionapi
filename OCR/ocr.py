def detect_text(path,imgurl):
    """Detects text in the file."""
    from google.cloud import vision
    import matplotlib.pyplot as plt 
    import matplotlib.patches as patches
    from PIL import Image
    import numpy as np
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    im = np.array(Image.open(imgurl), dtype=np.uint8)
    fix,ax = plt.subplots(1)
    ax.imshow(im)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print(texts[0])
    for text in texts:
        print(text.description)
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        # vertex direction: bottom left, bottom right, top right, top left
        #print(vertices[0])
        # bottom left
        (xlim_0,ylim_0) = strip_txt(vertices[0])
        # bottom right
        (xlim_1,ylim_1) = strip_txt(vertices[1])
        # top right
        (xlim_2,ylim_2) = strip_txt(vertices[3])
        width = xlim_1 - xlim_0
        height = ylim_2 - ylim_1
        rect = patches.Rectangle((xlim_0,ylim_0),width,height,linewidth=3,edgecolor='blue',facecolor='none')
        ax.add_patch(rect)
        #print(vertices[0][1:4])
    plt.show()


def strip_txt(string):
    accum1 = ''
    accum2 = ''
    i = 1
    while string[i] != ',':
        accum1 = accum1 + string[i]
        i = i + 1
    i = i + 1
    while string[i] != ')' and i < len(string):
        accum2 = accum2 + string[i]
        i = i + 1
    return (int(accum1),int(accum2))


def run():
    import time
    import os
    from os import listdir
    from os.path import isfile, join
    mypath = "/Users/robinlin/Desktop/Code/visionapi/OCR"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    jpg = []
    for i in onlyfiles:
        if ".jpg" in i:
            jpg.append(i)
    for i in jpg:
        file_name = os.path.abspath(i)
        print(file_name)
        detect_text(file_name,file_name)



detect_text("/Users/robinlin/Desktop/Code/visionapi/OCR/math2.jpg","math2.jpg")



