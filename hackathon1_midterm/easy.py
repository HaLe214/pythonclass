# 1
from datetime import datetime
import re

def day_diff(release_date, code_complete_day):
    d1 = datetime.strptime(release_date, "%d/%m/%Y")
    d2 = datetime.strptime(code_complete_day, "%Y-%d-%m")
    return d1 - d2


# 2
def alpha_num(sentence):
    #list_sent = sentence.split()
    #out = []
    #for s in list_sent:
    #    if re.search('\d', s) and re.search('[a-zA-Z]', s):
    #        out.append(s)
    regex = "\w+\d"
    out = re.findall(regex, sentence)
    return out

if __name__ == '__main__':
    print(alpha_num("Emma25 is 1 scientist50 AND AI Expert"))
