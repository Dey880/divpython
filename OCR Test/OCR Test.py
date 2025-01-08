import time
import pyautogui
import pytesseract
from PIL import Image
import os

pyautogui.FAILSAFE = True

region = (520, 80, 900, 120)

tesseract_cmd = r'C:\Users\Julian (skole)\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def sanitize_text(text):
    # Replace specific characters or add any additional sanitization as needed
    replacements = {
        "‘": "'",
        "’": "'",
        "|": "i",
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    return text

def capture_and_type_word(region, tesseract_cmd):
    
    # Set the path for the Tesseract OCR executable
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    # Capture the region of the screen
    screenshot = pyautogui.screenshot(region=region)
    
    # Save the screenshot to a file
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)
    
    # Open the screenshot
    image = Image.open(screenshot_path)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    # Sanitize the text
    text = sanitize_text(text)
        
    text = text.lower()

    # Extract the first word
    words = text.strip().split()



    if words:
        word = words[0]
        
        word = word.lower()


        if word == "q" or word == "qo'" or word == "qo'2":
            word = "o'"
            print(f"uh oh \n{word}")

        # Use pyautogui to type the word
        pyautogui.typewrite(word)
    
    # Delete the screenshot file
    os.remove(screenshot_path)

while True:
    capture_and_type_word(region, tesseract_cmd)
    time.sleep(0.1)