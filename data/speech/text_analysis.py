import os
path = "/Users/qingyi/Documents/uchicago/courses/data_programming_for_public_policy_2/hw3"
for fname in os.listdir(path + "/refugee briefs"): 
        with open(f"{path}/refugee briefs/{fname}") as page: 
            text = page.read()
        # doc = nlp(text)
