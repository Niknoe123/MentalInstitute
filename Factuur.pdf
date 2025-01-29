import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle


output_folder = "PDF_INVOICE"
os.makedirs(output_folder, exist_ok=True)


pdf_filename = os.path.join(output_folder, "factuur_template.pdf")


c = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4


c.setFont("Helvetica-Bold", 18)
c.drawString(50, height - 50, "INVOICE")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 80, "Mental Institute")

c.setFont("Helvetica", 12)
c.drawString(50, height - 110, "Romboutslaan 34")
c.drawString(50, height - 125, "Dordrecht, 3312 KW")
c.drawString(50, height - 140, "Phone: 088-657-2657")
c.drawString(50, height - 155, "Email: Mentalinstitute@gmail.com")


c.setFont("Helvetica-Bold", 12)
c.drawString(350, height - 80, "DATE:")
c.drawString(350, height - 95, "INVOICE NO:")
c.drawString(350, height - 110, "BTW-Nummer:")

c.setFont("Helvetica", 12)
c.drawString(450, height - 80, "________") 
c.drawString(450, height - 95, "________") 
c.drawString(450, height - 110, "NL12345678B01")

c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 180, "INVOICE TO:")
c.setFont("Helvetica", 12)
c.drawString(50, height - 195, "Street Address")
c.drawString(50, height - 210, "City, ST ZIP Code")
c.drawString(50, height - 225, "Phone: ________")
c.drawString(50, height - 240, "Email: ________")


table_data = [
    ["Quantity", "Description", "Unit Price", "Line Total"],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
]

table = Table(table_data, colWidths=[100, 250, 100, 100])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
]))


table.wrapOn(c, width, height)
table.drawOn(c, 50, height - 400)

c.setFont("Helvetica-Bold", 12)
c.drawString(350, height - 450, "Subtotal:")
c.drawString(350, height - 470, "Sales Tax:")
c.drawString(350, height - 490, "Total:")

c.setFont("Helvetica", 12)
c.drawString(450, height - 450, "________")
c.drawString(450, height - 470, "________")
c.drawString(450, height - 490, "________")


c.showPage()
c.save()

print(f"PDF opgeslagen als: {pdf_filename}")
os.startfile(pdf_filename)