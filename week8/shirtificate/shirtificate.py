from fpdf import FPDF
from PIL import Image


pdf = FPDF()
pdf.add_page() # Create the pdf
pdf.set_font('Helvetica', 'B', size=50)
# Make the header text
pdf.cell(0, 50, text='CS50 Shirtificate', align='C', new_x='LMARGIN', new_y='NEXT')
# Put in the shirtificate img
pdf.image('shirtificate.png', x=5, y=80, w=200)
pdf.set_font('Helvetica', style='B', size=30)
pdf.set_text_color(255, 255, 255)
# Create the text with your name on it
pdf.cell(0, 180, align='C', text=input('Name: ') + ' took CS50')
pdf.output('shirtificate.pdf')
