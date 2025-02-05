Document Classification and Extraction API
Overview
This API provides automatic classification and data extraction for documents such as invoices, emails, and budgets. Using machine learning for document classification and regular expressions for data extraction, it is designed to process both PDF and image files. For images, Optical Character Recognition (OCR) is used to extract the text and perform the necessary operations.

Features
Document Classification: Classify documents into predefined categories such as:

Invoice
Email
Budget
(Add more categories as needed)
Invoice Extraction: When a document is classified as an invoice, the API extracts the following key fields:

Invoice Number
Date
Amount
Vendor Name
Supports PDF and Image Files: Extract text from both PDF and image files, leveraging OCR to process images.

Requirements
Python 3.x
Required Python libraries (listed in requirements.txt):
Flask
pytesseract (OCR)
pdfplumber (for extracting text from PDFs)
Pillow
scikit-learn
pandas
numpy
re (for regular expressions)
Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/document-classification-extraction-api.git
cd document-classification-extraction-api
Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install Tesseract OCR (if not already installed):

Windows: Download from here and add the installation path to your system environment variables.
Linux: Run sudo apt-get install tesseract-ocr
macOS: Use brew install tesseract
API Endpoints
1. POST /classify_document
Classifies the uploaded document and returns its category.

Request:

file: The document file (PDF or image)
Response:

json
Copy
Edit
{
  "status": "success",
  "category": "invoice" // or other category like 'email', 'budget', etc.
}
2. POST /extract_invoice_data
Extracts invoice details from a document classified as an invoice.

Request:

file: The document file (PDF or image)
Response:

json
Copy
Edit
{
  "status": "success",
  "invoice_number": "12345",
  "date": "2025-02-05",
  "amount": "200.50",
  "vendor": "ABC Corp"
}
Usage
Classify a Document:
Use the /classify_document endpoint to classify a document. You can upload PDFs or image files, and the system will return the category.

Extract Invoice Data:
After classifying the document as an invoice, use the /extract_invoice_data endpoint to extract relevant invoice fields such as invoice number, date, amount, and vendor name.

Example
To classify a document:

bash
Copy
Edit
curl -X POST -F "file=@invoice.pdf" http://localhost:5000/classify_document
To extract invoice data:

bash
Copy
Edit
curl -X POST -F "file=@invoice.pdf" http://localhost:5000/extract_invoice_data
Development
Running Locally
Start the API server:

bash
Copy
Edit
flask run
The API will be available at http://localhost:5000.

Testing
Include your test cases in the tests/ directory. You can use pytest to run the tests:

bash
Copy
Edit
pytest tests/
Contributing
Feel free to fork this project and submit pull requests. For any suggestions or issues, open an issue on GitHub.





