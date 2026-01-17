num = int(input())
arr = []
for i in range(num):
        arr.append(input())
for a in arr:
        temp = a.split("=")
        countx = 0
        countc = 0
        current = len(temp[0])-1
        while current >= 0:
                if temp[0][current] == "x":
                        current -= 1
                        xnumber = ""
                        while temp[0][current] != "+" and temp[0][current] != "-" and current >= 0:
                                xnumber = temp[0][current] + xnumber
                                current -= 1
                        if current >= 0 and temp[0][current] == "-":
                                if xnumber == "":
                                        countx -= 1
                                else:
                                        countx -= int(xnumber)
                        else:
                                if xnumber == "":
                                        countx += 1
                                else:
                                        countx += int(xnumber)
                elif temp[0][current] != "x" and temp[0][current] != "+" and temp[0][current] != "-":
                        cnumber = ""
                        while temp[0][current] != "+" and temp[0][current] != "-" and current >= 0:
                                cnumber = temp[0][current] + cnumber
                                current -= 1
                        if current >= 0 and temp[0][current] == "-":
                                countc += int(cnumber)
                        else:
                                countc -= int(cnumber)
                current -= 1
        current = len(temp[1])-1
        while current >= 0:
                if temp[1][current] == "x":
                        current -= 1
                        xnumber = ""
                        while temp[1][current] != "+" and temp[1][current] != "-" and current >= 0:
                                xnumber = temp[1][current] + xnumber
                                current -= 1
                        if current >= 0 and temp[1][current] == "-":
                                if xnumber == "":
                                        countx += 1
                                else:
                                        countx += int(xnumber)
                        else:
                                if xnumber == "":
                                        countx -= 1
                                else:
                                        countx -= int(xnumber)
                elif temp[1][current] != "x" and temp[1][current] != "+" and temp[1][current] != "-":
                        cnumber = ""
                        while temp[1][current] != "+" and temp[1][current] != "-" and current >= 0:
                                cnumber = temp[1][current] + cnumber
                                current -= 1
                        if current >= 0 and temp[1][current] == "-":
                                countc -= int(cnumber)
                        else:
                                countc += int(cnumber)
                current -= 1
        if countx == 0 and countc == 0:
                print("IDENTITY")
        elif countx == 0 and countc != 0:
                print("IMPOSSIBLE")
        else:
                print(countc//countx)