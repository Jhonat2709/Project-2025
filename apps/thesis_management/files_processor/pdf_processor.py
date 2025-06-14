from io import BytesIO
from PyPDF2 import PdfReader


def get_pdf_buffer(pdf_file):
    # Read the file in memory (BytesIO act like a virtual memory "virtual file")
    pdf_bytes = pdf_file.read()

    # Create a byte buffer
    pdf_buffer = BytesIO(pdf_bytes)

    return pdf_buffer


def create_pdf_buffer(pdf_file):
    pdf_buffer = pdf_file.read()
    return BytesIO(pdf_buffer)


def handle_uploaded_pdf(buffer):
    buffer.seek(0)  # Reset the buffer position to the beginning
    text = ""
    try:
        reader = PdfReader(buffer)
        for page in reader.pages:
            text += page.extract_text() + "\n\n"
    except Exception as e:
        return f"Error leyendo PDF: {str(e)}"
    return text


def get_pdf_pages(buffer):
    buffer.seek(0)  # Reset the buffer position to the beginning
    # Return the quantity of pages of the pdf file
    reader = PdfReader(buffer)
    num_pages = len(reader.pages)  # Ensure the reader is initialized
    return num_pages
