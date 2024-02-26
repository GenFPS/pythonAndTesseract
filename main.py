import os
from PIL import Image
from pytesseract import pytesseract

local_app_data = os.environ['LOCALAPPDATA']

tesseract_path = os.path.join(local_app_data, 'Programs', 'Tesseract-OCR')
img_path = r'assets\img.png'

img = Image.open(img_path)

# Предоставляем установленный на локальном ПК tesseract для lib pytesseract
pytesseract.tesseract_cmd = tesseract_path

parsed_imgText = pytesseract.image_to_string(img)

if __name__ == '__main__':
    try:
        print(parsed_imgText)
    finally:
        print('The script has been completed')
