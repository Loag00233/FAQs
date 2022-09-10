simv, v1, v2, t1, t2 =  map(int, input().split())
speed1 = t1+(simv*v1)+t1
speed2 = t2+(simv*v2)+t2

if speed1 < speed2:
    print('First')
else:
    if speed1 == speed2:
        print('Friendship')
    else:
        print('Second')
