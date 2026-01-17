history = []
result = []
number = ('0','1','2','3','4','5','6','7','8','9')
import re
while True:
    text = input()
    if text == "0":break
    if text == "":continue
    non_list = re.findall(r'[^\w]' , text)
    alph = re.findall(r'[a-zA-Z]' , text)
    t = 0
    while t < len(text):
        if text[t] in non_list or text[t] == ' ':
            print(text[t] , end='')
        elif text[t] in number:
            num = ''
            while t < len(text) and text[t] in number:
                num += text[t]
                t += 1
            t -= 1
            num = int(num)
            print(history[num-1] , end='')
            temp = history[num-1]
            del history[num-1]
            history.insert(0 , temp)
        else:
            word = ''
            while t < len(text) and text[t] in alph:
                word += text[t]
                t += 1
            t -= 1
            history.insert(0 , word)
            print(word , end='')
        t += 1
    print()