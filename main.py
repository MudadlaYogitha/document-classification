from fastapi import FastAPI, UploadFile, File
import shutil
import os
import joblib
from preprocessing import extract_text_from_pdf, extract_text_from_image
from invoice_extraction import extract_invoice_fields

app = FastAPI()

# Load trained model and vectorizer
clf = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Ensure 'temp' directory exists
if not os.path.exists('temp'):
    os.makedirs('temp')

@app.post("/classify_and_extract")
async def classify_and_extract(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}, content type: {file.content_type}")  # Debugging
    
    # Save the uploaded file temporarily
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Extract text from the file
        if file.filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file.filename.endswith(('.jpg', '.png')):
            text = extract_text_from_image(file_path)
        else:
            return {"error": "Unsupported file format"}

        # Classify document
        X_test = vectorizer.transform([text])
        prediction = clf.predict(X_test)[0]

        # Extract invoice data if classified as invoice
        if prediction == "invoice":
            extracted_data = extract_invoice_fields(text)
            return {"classification": prediction, "extracted_data": extracted_data}

        return {"classification": prediction}

    finally:
        # Clean up: remove the uploaded file after processing
        os.remove(file_path)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}")
    print(f"File content type: {file.content_type}")
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

