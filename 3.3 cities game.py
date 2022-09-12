city1 = str(input().lower())
city2 = str(input().lower())

if city1[-1] == city2[0]:
    print('Good')
else:
    if city1[-1] == 'ь':
        if city1[-2] == city2[0]:
            print('Good')
        else:
            print('Bad')
    else:
        print('Bad')

