# document-classification
# Document Classification and Extraction API

This project provides an API to classify documents (such as invoices) and extract important fields like invoice number, date, amount, and vendor. It uses machine learning for document classification and regular expressions to extract specific data from invoices.

## Features
- **Document Classification**: Classify documents into categories like invoice, email, or budget.
- **Invoice Extraction**: If the document is classified as an invoice, key information (invoice number, date, amount, vendor) is extracted.
- **Supports PDF and Image Files**: Extract text from both PDFs and image files using OCR.


->API Endpoints
POST /classify_and_extract
Classifies the document (PDF or image) and extracts invoice fields if classified as an invoice.

Request
file (required): Upload the document (PDF or image) as part of the form data.
Example (using Postman or cURL):
Postman:

Select POST method.
Enter the URL: http://127.0.0.1:8000/classify_and_extract.
In the "Body" tab, choose "form-data" and add a key named file with the file to be uploaded.

->Evaluation
Classification Accuracy
The classification model has been evaluated using the classification_report metric. Here’s the result from the evaluation:

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





