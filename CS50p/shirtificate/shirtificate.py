# Code created by Pepijn Weitzel
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 50)
        # Move cursor down
        self.ln(10)
        # Move cursor
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")

# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", 10, 60, 190)
pdf.output("shirtificate.pdf")
