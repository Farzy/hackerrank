#!/bin/python3


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    common_len = 0
    s_total = len(s)
    t_total = len(t)
    while common_len < min(s_total, t_total) and \
            s[common_len] == t[common_len]:
        common_len += 1
    extra_delete_moves = k - s_total - t_total + 2 * common_len
    if (0 <= extra_delete_moves <= common_len * 2 and extra_delete_moves % 2 == 0) or \
            extra_delete_moves > common_len * 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
