# Merge-pdf-files-using-PyPDF2

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contribution](#contribution)


## Project Overview
The Python script demonstrates how to merge multiple PDF files found in the current directory into a single PDF document using the PyPDF2 library.
The script begins by creating a PdfWriter object named `merger` from the PyPDF2 library. It then identifies all PDF files in the current directory by filtering files with the ".pdf" extension using `os.listdir()`. Each PDF file is sequentially added to the `merger` object using the `append()` method. Once all PDFs are appended, the combined content is written to a new PDF file named "merged.pdf" using the `write()` method. Finally, the `merger` object is closed to release resources.


## Installation
This project requires Python 3.12.1 or later.
To set up the project:
1. Ensure Python 3.12.1 or a later version is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository to your local machine.
   
            git clone https://github.com/jaiswalchitransh/Merge-pdf-files-using-PyPDF2

4. Open the project in your preferred Python environment (e.g., IDE or terminal).
5. Install PyPDF2 library using pip:
   
            pip install PyPDF2 

6. Run the script (`merger.py`) and observe the output.


## Usage
Run the script:

            python merger.py
  
After execution, a file named "merged.pdf" will be created in the same directory containing the merged PDF content.


## Features
- **Simple Interface**: Combines PDF files with minimal configuration.
- **Automatic File Detection**: Identifies and merges all PDF files in the current directory.
- **Efficient Resource Management**: Properly closes resources after merging.


## Contribution
I, **Chitransh Jaiswal** developed this Project Individually. I was responsible for all aspects of the project, including design, development, testing, and documentation.
Contributions to improve the efficiency, readability, or functionality of the code are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

Please ensure your contributions adhere to the coding standards and follow the existing style and structure.

---

Thank you for your interest in the PDF Merger using PyPDF2. Have fun Merging your PDFs!
