def check(num):
    div = []
    for n in range(1,(num+1)):
        if num%n == 0:
            div.append(n)
    if len(div)==2:

        print(True)
    else:
        print(False)
check(23)
