#!/bin/python3


# Complete the dayOfProgrammer function below.
def day_of_programmer(year):
    def leap(year):
        if year < 1917:
            if year % 4 == 0:
                return 1
            else:
                return 0
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 1
        else:
            return 0

    if year != 1918:
        return "{0:02d}.09.{1:04d}".format(13 - leap(year), year)
    else:
        return "26.09.1918"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = day_of_programmer(year)

    # fptr.write(result + '\n')

    # fptr.close()

    print(result)
