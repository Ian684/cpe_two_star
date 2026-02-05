while True:
    months , pay , value , n = input().split()
    if int(months) < 0:break
    months , n = int(months) , int(n)
    pay , value = float(pay) , float(value)
    arr = {}
    for i in range(n):
        a , b = input().split()
        a = int(a)
        b = 1.000 - float("0" + b)
        arr[a] = b
    t = arr[0]
    every = value / months
    owe = value
    value += pay
    value *= t
    result = months
    if owe < value:
        result = 0
    else:
        for i in range(1 , months + 1):
            owe -= every
            if i in arr:
                t = arr[i]
            value *= t
            if owe < value:
                result = i
                break
    if result == 1:
        print(result , "month")
    else:
        print(result , "months")
        
    
