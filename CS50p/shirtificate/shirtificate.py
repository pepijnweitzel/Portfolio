# Code created by Pepijn Weitzel
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
