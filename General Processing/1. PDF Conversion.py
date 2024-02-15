import os
import Cryptodome
from PyPDF2 import PdfReader
from Cryptodome.Cipher import AES

folder_path = "PDF Data Set/E-government"


# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PDF
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)
        # Open the PDF file
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
        # Create the text file with same name and different extension
            text_file_path = os.path.splitext(file_path)[0] + ".txt"
        # Open the text file to write the contents of the PDF
            with open(text_file_path, 'w') as text_file:
            # Iterate through each page of the PDF
                for page in range(len(pdf.pages)):
                # Extract the text from the page
                    text = pdf.pages[page].extract_text()
                # Write the text to the text file
                    text_file.write(text)
                # Delete the original pdf file
                os.remove(file_path)