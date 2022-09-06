import pathlib

from PyPDF2 import PdfReader

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

pdf_in = files_path.joinpath("Joshua Block - Effective Java (3rd) - 2018.pdf")

reader = PdfReader(pdf_in)


p1 = reader.pages[15]


print(reader.numPages)