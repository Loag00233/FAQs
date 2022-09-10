a, b, c = map(int, input().split())

if a > b and b > c and a > c:
    print(a - c)
else:
    if a > b and b < c and a > c:
        print(a - b)
    else:
        if a < b and b > c and a > c:
            print(b - c)
        else:
            if a < b and b < c and c > a:
                print(c - a)
            else:
                if a < b and b > c and a < c:
                    print(b - a)
                else:
                    print(c - b)

