import re

def extract_invoice_fields(text):
    # Regular expression patterns
    invoice_number_pattern = r'(Invoice\s*No\.\s*|\bInvoice\s*#\s*)(\S+)'  # Flexibility for invoice number
    date_pattern = r'(Date|Issued)\s*[:\-]?\s*([\d]{2}[-/.\s]?\d{2}[-/.\s]?\d{4}|\d{4}[-/.\s]?\d{2}[-/.\s]?\d{2})'
    amount_pattern = r'(Total\s*Amount|Amount\s*Due)\s*[:\-]?\s*(\$?[\d,.]+)'  # More flexible for amounts
    vendor_pattern = r'(Vendor|Supplier)\s*[:\-]?\s*(.*)'

    # Searching for the fields
    invoice_number = re.search(invoice_number_pattern, text)
    date = re.search(date_pattern, text)
    amount = re.search(amount_pattern, text)
    vendor = re.search(vendor_pattern, text)

    # Return the fields found, or None if not found
    return {
        'invoice_number': invoice_number.group(2) if invoice_number else None,
        'date': date.group(2) if date else None,
        'amount': amount.group(2) if amount else None,
        'vendor': vendor.group(2) if vendor else None
    }



