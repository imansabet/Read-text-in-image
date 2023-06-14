# Read-text-in-image
# Image to Text Converter
This Python program uses the Tesseract OCR engine to convert images to text. The program takes an image file as input, extracts the text from the image using Tesseract, and writes the text to a text file.

The program can also draw bounding boxes around the text in the original image and display the image with the bounding boxes.

# Installation
# Step 1: 
Install Tesseract
Before running the program, you must install Tesseract on your system. You can download and install Tesseract from the following link: (https://github.com/UB-Mannheim/tesseract/wiki)

# Step 2: 
Install Python Packages
You will need to install the following Python packages to run the program:

pytesseract
PIL
opencv-python
matplotlib
You can install these packages using pip:


```pip install pytesseract Pillow opencv-python matplotlib```

# Step 3:
Clone the Repository
Clone this repository to your local machine using the following command:


```git clone https://github.com/yourusername/img-to-text.git```
# Step 4: Run the Program

To run the program, navigate to the project directory and run the following command:


```python img_to_text.py
This will convert the sample images in the images directory to text and write the text to the text.txt file.
