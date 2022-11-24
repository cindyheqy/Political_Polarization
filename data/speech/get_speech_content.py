# import os
# path = "/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/hw3"
# for fname in os.listdir(path + "/refugee briefs"): 
#         with open(f"{path}/refugee briefs/{fname}") as page: 
#             text = page.read()
#         # doc = nlp(text)


import os
import re
path = "/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/Political_Polarization/data/speech/speech_data_txt"

speech_date = {}
def get_speech(text): 
    pattern = r"(M[a-z]+. [A-Z]+. M[a-z]+. Speaker,(?s).*)"
    # match = re.findall(pattern, text)
    match = re.search(pattern, text)
    if match: 
    # assert(match), f'No match for country: '
        return match.group(1)
# need to 弄成所有的speech，现在只有单个的，接在后面用加号，换行，连接成一个文本

flag = 0
m = False

for fname in os.listdir(path): 
        with open(f"{path}/{fname}") as page: 
            match_mrspeaker = 0
            count_thespeaker = 0
            date = fname.split('.')[0]
            # if len(speech_text) >= 1: 
            flag += 1
            if flag < 30:
                text = page.read()
                # text = text.split('THE SPEAKER')
                m = False
                for sub_text in text.split('THE SPEAKER'): 
                    count_thespeaker += 1
                    # match_speaker = 0
                    speech_text = get_speech(sub_text)
                    if speech_text: 
                        match_mrspeaker += 1
                        m = True
                        if date not in speech_date.keys(): 
                            speech_date[date] = speech_text
                        else: 
                            speech_date[date] += speech_text
                if m == False: 
                    print(date, "no match today!")
                print(date, count_thespeaker, match_mrspeaker)
                
            else: 
                break
# print(speech_date)

print(speech_date.keys())
            # break
            