from datetime import date


# Complete the libraryFine function below.
def library_fine(d1, m1, y1, d2, m2, y2):
    date1 = date(year=y1, month=m1, day=d1)
    date2 = date(year=y2, month=m2, day=d2)

    if date1 <= date2:
        return 0
    elif (m1, y1) == (m2, y2):
        return (d1- d2) * 15
    elif y1 == y2:
        return (m1 - m2) * 500
    else:
        return 10_000


if __name__ == '__main__':
    d1, m1, y1 = map(int, input().split())
    d2, m2, y2 = map(int, input().split())

    result = library_fine(d1, m1, y1, d2, m2, y2)

    print(result)
