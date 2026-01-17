# 純暴力
ans_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans_2 = []
ans_3 = []
ans_4 = []
ans_5 = []
for i in ans_1:
    for j in ans_1[1:]:
        if i[-1] < j:
            ans_2.append(i+j)
for i in ans_2:
    for j in ans_1[2:]:
        if i[-1] < j:
            ans_3.append(i+j)
for i in ans_3:
    for j in ans_1[3:]:
        if i[-1] < j:
            ans_4.append(i+j)
for i in ans_4:
    for j in ans_1[4:]:
        if i[-1] < j:
            ans_5.append(i+j)
ans = ans_1 + ans_2 + ans_3 + ans_4 + ans_5
while True:
    try:
        text = input()
        if text in ans:
            print(ans.index(text)+1)
        else:
            print(0)
    except EOFError:
        break