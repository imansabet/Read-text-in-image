import cv2
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# Set the name of the output file
filename = 'savedImage.jpg'

# Load the image using OpenCV
image = cv2.imread("C:/Users/Administrator/Desktop/python/img_to_text/images/1.jpg")

# Extract the text from the image using Tesseract
img_text = pytesseract.image_to_string(image)

# Extract the position of every word in the image using Tesseract
text_boxes = pytesseract.image_to_boxes(image)

# Extract the data for every word in the image using Tesseract
img_data = pytesseract.image_to_data(image, output_type=Output.DICT)
w, h, c = image.shape

# Draw a rectangle around every word in the image using OpenCV
for index, text in enumerate(img_data['text']):
    if text:
        x1 = int(img_data['left'][index])
        y1 = int(img_data['top'][index])
        x2 = x1 + int(img_data['width'][index])
        y2 = y1 + int(img_data['height'][index])
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Save the image with rectangles around the words
cv2.imwrite(filename, image)

# Display the image with rectangles around the words using OpenCV
cv2.imshow('image', image)

# Wait for the user to press a key
k = cv2.waitKey(0)