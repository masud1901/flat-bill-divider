import bill, flatmate
from fpdf import FPDF


class PdfReport:
    """Creates a PDF report of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Add period and amount
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.cell(w=100, h=40, txt="Total Amount:", border=0)
        pdf.cell(w=150, h=40, txt=str(bill.amount), border=0, ln=1)

        # Add header for flatmate details
        pdf.cell(w=0, h=20, txt="Flatmate Details:", border=0, ln=1)
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=160, h=30, txt="Name", border=1)
        pdf.cell(w=100, h=30, txt="Days in House", border=1)
        pdf.cell(w=100, h=30, txt="Amount to Pay", border=1, ln=1)

        # Add flatmate details
        for flatmate in flatmates:
            pdf.cell(w=160, h=30, txt=flatmate.name, border=1)
            pdf.cell(w=100, h=30, txt=str(flatmate.days_in_house), border=1)
            pdf.cell(
                w=100,
                h=30,
                txt=str(flatmate.payment),
                border=1,
                ln=1,
            )

        # Save the PDF
        pdf.output(self.filename)
        print(f"PDF report generated: {self.filename}")
