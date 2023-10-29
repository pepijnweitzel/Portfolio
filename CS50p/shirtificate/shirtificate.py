# Code created by Pepijn Weitzel
from fpdf import FPDF

def main():

    # Prompt user for name
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, name)
    pdf.output("tuto1.pdf")



if __name__ == "__main__":
    main()
