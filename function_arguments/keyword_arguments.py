def func1(a, b, c):
    print(a, b, c)


func1(1, 2, 3)

func1(1, c=3, b=2)


def func1(a, b, *args, d):
    print(a, b, args, d)


func1(1, 2, 3, 4, d=4)
