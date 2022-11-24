import os
import re
path = "/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech"

speech_date = {}

def get_speech(text): 
    pattern = r"(M[a-z]+. [A-Z]+. M[a-z]+. Speaker,(?s).*)" # content starts with Mr/Madam Speaker
    match = re.search(pattern, text)
    if match: 
        return match.group(1)

for fname in os.listdir(os.path.join(path, "speech_data_txt")): 
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
            # if m == False: 
            #     print(date, "no match today!")
            # print(date, count_thespeaker, match_mrspeaker)
            if has_speech == True: 
                with open(f"{path}/speech_data_content/{fname}", 'w', encoding='utf-8') as ofile:
                    ofile.write(speech_date[date]) # save speech content
            