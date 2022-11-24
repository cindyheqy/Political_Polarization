import requests
import PyPDF2
import datetime

# specify record time rage
start_date = datetime. date(2017, 1, 1)
end_date = datetime. date(2017, 12, 30)
delta = datetime. timedelta(days=1)

output_path = "Political_Polarization/data/speech"
date_no_record = open(f"{output_path}/date_no_record.txt","w") 

while start_date <= end_date:
    path = f"https://api.govinfo.gov/packages/CREC-{start_date}/pdf?api_key=BsveU3Pa1wRgMsVrb6lNXkSdBub4OtEq0OMshRdp"
    response = requests.get(path)
    if response.ok:
        with open(f"{output_path}/speech_data_pdf/{start_date}.pdf", 'wb') as ofile:
            ofile.write(response.content) # save pdf file
        # convert pdf to txt
        pdf = PyPDF2.PdfFileReader(f"{output_path}/speech_data_pdf/{start_date}.pdf", strict=False)
        text = []
        for pnum in range(pdf.getNumPages()):
            page = pdf.getPage(pnum)
            text.append(page.extractText())
        full_text = '\n'.join(text) 
        with open(f"{output_path}/speech_data_txt/{start_date}.txt", 'w', encoding='utf-8') as ofile:
            ofile.write(full_text) # save txt file
    else:
        print(start_date, file=date_no_record) # date with no response
    start_date += delta
date_no_record.close()