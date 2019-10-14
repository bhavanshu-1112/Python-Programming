def dayofweek(d, m, y):
    t = [0, 3, 2, 5, 0, 3,
         5, 1, 4, 6, 2, 4]
    y -= m < 3
    return ((y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)


dd = int(input("enter day : "))
mm = int(input("enter month : "))
yy = int(input("enter year : "))
day = dayofweek(dd, mm, yy)
if day is 0:
    print("Sunday")
elif day is 1:
    print("Monday")
elif day is 2:
    print("Tuesday")
elif day is 3:
    print("Wednesday")
elif day is 4:
    print("Thrusday")
elif day is 5:
    print("Friday")
elif day is 6:
    print("Saturday")