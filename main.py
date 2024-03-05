from fpdf import FPDF
import pandas as pd;


pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='times', size=25)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align='C')

    for y in range(20,298,10):
        pdf.line(10, y, 200, y)

    for i in range (row["Pages"] - 1):
            pdf.add_page()
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

pdf.output("notebook.pdf")
