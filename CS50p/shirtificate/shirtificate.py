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

    def body(self):
        # Import image
        self.image("shirtificate.png", 10, 60, 190)

    def printing(self, name):
        # Move cursor down
        self.ln(100)
        # Set font
        self.set_font("helvetica", "B", 25)
        # Set color to white
        self.set_text_color(255, 255, 255)
        # Print name with "took CS50"
        self.cell(200, 10, f"{name} took CS50", align="C")

def main():
    # Create file and set body and header
    pdf = PDF()
    pdf.add_page()
    pdf.body()

    name = input("Name: ")

    pdf.printing(name)


    # Output the file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
