### File in <proj_home>/downloads/textSearchReplace/captions_text.vtt
### Goal to find all 4 letter words

import os
import re

def start_job(fl):
    all_text = fl.read()
    print(re(all_text))

if __name__ == "__main__":
    print(os.system("pwd"))
    #print(os.system("ls ../../downloads/MasterPython_CodeAndData/"))
    with open("../../downloads/MasterPython_CodeAndData/textSearchReplace/captions_text.vtt", "r") as fl:
        start_job(fl)