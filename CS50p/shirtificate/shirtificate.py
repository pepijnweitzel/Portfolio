# Code created by Pepijn Weitzel
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.text(30, 10, "CS50 Shirtificate")

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
