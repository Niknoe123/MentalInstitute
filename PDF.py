import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Vraag om gebruikersinvoer
user_text = input("Voer de tekst in voor de PDF: ")

# Zorg ervoor dat de opslagmap bestaat
output_folder = "PDF_INVOICE"
os.makedirs(output_folder, exist_ok=True)

# Bestandsnaam en pad
pdf_filename = os.path.join(output_folder, "generated.pdf")

# PDF genereren
c = canvas.Canvas(pdf_filename, pagesize=A4)
width, height = A4  # A4-formaat

# Voeg tekst toe in het midden van de pagina
c.setFont("Helvetica", 16)
text_x = width / 2
text_y = height / 2
c.drawCentredString(text_x, text_y, user_text)

# Opslaan en sluiten
c.showPage()
c.save()

print(f"PDF opgeslagen als: {pdf_filename}")
