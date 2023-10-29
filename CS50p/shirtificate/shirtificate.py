# Code created by Pepijn Weitzel
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font:
        self.set_font("helvetica", "B", 16)
        # Printing title:
        self.cell(100, 10, "CS50 Shirtificate", border=1, align="C")


def main():

    # Prompt user for name
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.header()
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()
