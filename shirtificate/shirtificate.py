from fpdf import FPDF


def create_pdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=32)
    pdf.cell(200, 25, 'CS50 Shirtificate', new_x="LMARGIN", align='C')
    pdf.image("./shirtificate.png", 5, 50, 200)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255)
    pdf.cell(200, 250, f'{name} took CS50', align='C')
    pdf.output("shirtificate.pdf")

def main():
    create_pdf(input("Name: "))


if __name__ == "__main__":
    main()
