import requests
import os
import PyPDF2

path = "https://api.govinfo.gov/packages/CREC-2019-02-04/pdf?api_key=BsveU3Pa1wRgMsVrb6lNXkSdBub4OtEq0OMshRdp"
response = requests.get(path)

fname = path.split('/')[4]
with open(f"speech/{fname}.pdf", 'wb') as ofile:
    ofile.write(response.content)

pdf = PyPDF2.PdfFileReader(f"speech/{fname}.pdf")
pdf.getNumPages()
# os.remove(f"speech/{fname}")
text = []
for pnum in range(pdf.getNumPages()):
    page = pdf.getPage(pnum)
    text.append(page.extractText())
full_text = '\n'.join(text)
with open(os.path.join(f"speech/{fname}.txt"), 'w', encoding='utf-8') as ofile:
    ofile.write(full_text)