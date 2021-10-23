def multiple(x, y):
    return x * y

def add(x, y):
    return x + y

def myfunc(z,  u):
    return z + u
def newfunc(z, u):
    return z / u
print(newfunc(210, 500))
print(myfunc(210, 500), 2)

def season(month):
    if month == 12 or month < 3:
        return 'winter'
    elif month == 3 or month < 6:
        return 'spring'
    elif month == 6 or month < 9:
        return 'summer'
    elif month == 9 or month < 11:
        return 'autumn'
    else:
        return ' error'


def bank(a, years):
    deposit = a
    koef = 2
    year = 1
    while year <= years:
        deposit = koef * deposit
        year += 1
        return deposit

def bank1(a, years):
    years = years + 1
    for i in range(1, years):
        summazagod = a * 0.1 + a
        a = summazagod
        print(a)

if __name__ == '__main__':
    print(bank1(1000, 5))
    print(newfunc(210, 500))
    print(myfunc(210, 500), 2)