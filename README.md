# document-classification

# Document Classification and Extraction API

This project provides an API to classify documents (such as invoices) and extract important fields like invoice number, date, amount, and vendor. It uses machine learning for document classification and regular expressions to extract specific data from invoices.

## Features
- **Document Classification**: Classify documents into categories like invoice, email, or budget.
- **Invoice Extraction**: If the document is classified as an invoice, key information (invoice number, date, amount, vendor) is extracted.
- **Supports PDF and Image Files**: Extract text from both PDFs and image files using OCR.

## Installation

### Step 1: Clone the repository
Clone this repository to your local machine.

```bash
git clone https://github.com/username/document-classification.git
cd document-classification
Step 2: Set up the virtual environment
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
Activate the virtual environment:

Windows: env\Scripts\activate
macOS/Linux: source env/bin/activate
Step 3: Install dependencies
Install all required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the application
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
The application will be running at http://127.0.0.1:8000/.

API Endpoints
POST /classify_and_extract
Classifies the document (PDF or image) and extracts invoice fields if classified as an invoice.

Request
Upload a file (PDF or Image) as part of the form data.

Example (using Postman or cURL):

file (required): The document to classify and extract.
Response
If classified as an invoice:

json
Copy
Edit
{
  "classification": "invoice",
  "extracted_data": {
    "invoice_number": "12345",
    "date": "2022-01-01",
    "amount": "100.00",
    "vendor": "ABC Corp"
  }
}
If classified as another type:

json
Copy
Edit
{
  "classification": "email"
}
If unsupported file format:

json
Copy
Edit
{
  "error": "Unsupported file format"
}
Evaluation
Classification Accuracy
The classification accuracy of the model can be evaluated using classification_report. Here's a sample evaluation result:

plaintext
Copy
Edit
precision    recall  f1-score   support

invoice       0.91      0.89      0.90       100
email         0.89      0.92      0.90        99
budget        0.92      0.93      0.92       100

accuracy                           0.91       299
macro avg     0.91      0.91      0.91       299
weighted avg  0.91      0.91      0.91       299
Dependencies
fastapi - Web framework for building APIs.
uvicorn - ASGI server to run the FastAPI app.
joblib - For saving/loading the trained model.
pdfplumber - For extracting text from PDFs.
pytesseract - For Optical Character Recognition (OCR) to extract text from images.
pandas - For handling the dataset.
scikit-learn - For machine learning tasks like classification.
