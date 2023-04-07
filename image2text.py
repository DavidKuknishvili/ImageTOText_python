from flask import Flask, request, jsonify
import pytesseract
import requests
from PIL import Image
from io import BytesIO



def generator(image):

    response = requests.get(image)
    img = Image.open(BytesIO(response.content))
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
    grayscale_image = img.convert('L')
    text = pytesseract.image_to_string(grayscale_image, lang=None)

    grayscale_image.save('example_grayscale.jpg')
    return text


app = Flask(__name__)

@app.route('/api/process-image', methods=['POST'])
def process_image():
    image_url = ""
    if request.method == 'POST':
        image_url = request.form['image_url']

    response = {'text': generator(image_url)}
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
