import os
import re
path = "/Users/qingyihe/Documents/GitHub/Political_Polarization/data/speech"

speech_date = {}

def get_speech(text): 
    text = text.split('the President pro tempore')[0]
    pattern = r"(M[a-z]+. [A-Z]+. M[a-z]+. Speaker,(?s).*)" # content starts with Mr/Madam Speaker
    match = re.search(pattern, text)
    if match: 
        return match.group(1)

def clean_data(text): 
    new_text = re.sub('([A-Z|-])\n([A-Z]*)', r'\1\2', text)
    new_text = re.sub('([a-z]*)-([a-z]*)', r'\1\2', new_text)
    new_text = re.sub('IN THE HOUSE OF REPRESENTATIVES  .*, 2017 M', 'M', new_text)
    output = []
    new_text_lines = new_text.splitlines()
    for line in new_text_lines: 
        if (('CONGRESSIONAL RECORD' not in line) and 
            ('VerDate' not in line) and 
            (len(line.split()) > 8) and 
            (line.strip() != "f") and 
            (not re.search('(\([\d]+\)|\(\w\))', line)) and 
            ('sec.' not in line.lower()) and 
            ('(a)' not in line.lower()) and
            ('................' not in line)):
            output.append(line)
    new_text = "\n".join(output)
    return new_text

for fname in os.listdir(os.path.join(path, "speech_data_txt")): 
    # if fname.startswith('2016'):
        with open(f"{path}/speech_data_txt/{fname}") as page: 
            # match_mrspeaker = 0
            # count_thespeaker = 0
            date = fname.split('.')[0]
            text = page.read()
            has_speech = False
            for sub_text in text.split('THE SPEAKER'): 
                # count_thespeaker += 1
                # match_speaker = 0
                speech_text = get_speech(sub_text)
                if speech_text: 
                    # match_mrspeaker += 1
                    has_speech = True
                    if date not in speech_date.keys(): 
                        speech_date[date] = speech_text
                    else: 
                        speech_date[date] += speech_text
            # speech_date[]
            # if m == False: 
            #     print(date, "no match today!")
            # print(date, count_thespeaker, match_mrspeaker)
            # clean_content = {date: clean_data(content) for date, content in speech_date.items()}
            if has_speech == True: 
                speech_date[date] = clean_data(speech_date[date])
                with open(f"{path}/speech_data_content/{fname}", 'w', encoding='utf-8') as ofile:
                    ofile.write(speech_date[date]) # save speech content

# clean = clean_data(speech_date["2017-12-20"])
# with open(f"{path}/tmp.txt", 'w', encoding='utf-8') as ofile:
#     ofile.write(clean)