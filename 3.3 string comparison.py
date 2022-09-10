string1 = str(input().lower())
string2 = str(input().lower())
if string1 == string2:
    print(0)
else:
    if string1 > string2:
        print(1)
    else:
        print(-1)
