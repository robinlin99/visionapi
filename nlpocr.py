def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    import io
    client = vision.ImageAnnotatorClient()
    client_lang = language.LanguageServiceClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print(texts)
    textstr = ''
    print(texts)
    print('Texts:')
    for text in texts:
        print(text.description)
        textstr = textstr + ' ' + text.description

        '''
        print('\n"{}"'.format(text.description))
     
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
        '''
    document = types.Document(
    content=textstr,
    type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client_lang.analyze_sentiment(document=document).document_sentiment
    print(sentiment)

detect_text("/Users/robinlin/Desktop/Code/visionapi/OCR/docs.jpg")

