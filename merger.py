# Merge pdf files using PyPDF2
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
pdfs = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
