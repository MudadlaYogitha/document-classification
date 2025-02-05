import os
import pandas as pd
import pytesseract
import pdfplumber
from PIL import Image

# Load dataset containing file paths and categories
df = pd.read_csv('dataset/cleaned_data.csv')  
print(df.head())  # Display first few rows
print(df.info())  # Check dataset details

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

# Function to extract text from images using pytesseract (OCR)
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

# Apply text extraction based on file type
texts = []
for file_path in df['file_path']:
    if file_path.endswith(('.jpg', '.png', '.jpeg')):
        extracted_text = extract_text_from_image(file_path)
    elif file_path.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)
    else:
        extracted_text = "Unsupported file format"
    
    texts.append(extracted_text)

# Add extracted text to dataset
df['extracted_text'] = texts

# Save updated dataset with extracted text
df.to_csv('dataset/extracted_text.csv', index=False)
print("Extracted text saved!")
