number = ['0','1','2','3','4','5','6','7','8','9']
operator = ["+","-","*","/"]
while True:
        try:
                text = input().replace(" " , "")
                num = False
                arr = []
                docu = ""
                if text[0] in operator:
                        new = text[0]
                        t = 1
                else:
                        new = ''
                        t = 0
                while t < len(text):
                        if text[t] == "=":
                                arr.append(int(docu))
                                arr.append(text[t])
                                arr.append(text[t+1:])
                                break
                        elif num and text[t] in number:
                                docu += text[t]
                        elif not num and text[t] in number:
                                docu = new + text[t]
                                new = ''
                                num = True
                        elif num and text[t] in operator:
                                arr.append(int(docu))
                                num = False
                                arr.append(text[t])
                                if text[t+1] in operator:
                                        new += text[t+1]
                                        t += 1
                        t += 1
                i = 0
                while i < len(arr):
                    if arr[i] == "-":
                          if arr[i+1] == "+":
                                del arr[i+1]
                          elif arr[i+1] == "-":
                                arr[i] = "+"
                                del arr[i+1]
                    i += 1
                for i in arr:
                    print(i , end=" ")
                print()
                while True:
                    if "/" in arr and "*" in arr:
                        now = min(arr.index("*"),arr.index("/"))
                    elif "/" in arr:
                        now = arr.index("/")
                    elif "*" in arr:
                        now = arr.index("*")
                    else:
                        break
                    if arr[now] == "*":
                            arr[now] = arr[now-1]*arr[now+1]
                            del arr[now+1]
                            del arr[now-1]
                    elif arr[now] == "/":
                            arr[now] = arr[now-1]//arr[now+1]
                            del arr[now+1]
                            del arr[now-1]
                    for i in arr:
                            print(i , end=" ")
                    print()
                while True:
                    if "+" in arr and "-" in arr:
                        now = min(arr.index("+"),arr.index("-"))
                    elif "+" in arr:
                        now = arr.index("+")
                    elif "-" in arr:
                        now = arr.index("-")
                    else:
                        break
                    if arr[now] == "+":
                        arr[now] = arr[now-1]+arr[now+1]
                        del arr[now+1]
                        del arr[now-1]
                    elif arr[now] == "-":
                        arr[now] = arr[now-1]-arr[now+1]
                        del arr[now+1]
                        del arr[now-1]
                    for i in arr:
                        print(i , end=" ")
                    print()
                print()
        except EOFError:
                break