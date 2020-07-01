#!/bin/python3


# Previous version using permutations is too slow, this one is based on
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def biggerIsGreater(w):
    w_len = len(w)
    if w_len == 1:
        return "no answer"
    # As strings are immutable, work with a list
    w_list = list(w)
    # Find longest non-increasing suffix and the index of the element just before
    suffix_idx = None
    for i in range(w_len - 1, 0, -1):
        if w_list[i - 1] < w_list[i]:
            suffix_idx = i
            break
    if suffix_idx is None:
        return "no answer"
    pivot_idx = suffix_idx - 1
    # Find smallest element in suffix greater than pivot, furthest right
    smallest_idx = suffix_idx
    for i in range(suffix_idx + 1, w_len):
        if w_list[pivot_idx] < w_list[i] <= w_list[smallest_idx]:
            smallest_idx = i
    # print("String: {}, Pivot: {}, Suffix: {}, Smallest: {}".format(
    #       w, w[pivot_idx], w[suffix_idx:], w[smallest_idx]))
    # Swap pivot and smallest suffix element
    w_list[pivot_idx], w_list[smallest_idx] = w_list[smallest_idx], w_list[pivot_idx]
    # Sort (i.e reverse) suffix
    w_list = w_list[:suffix_idx] + list(reversed(w_list[suffix_idx:]))
    # return string
    return ''.join(w_list)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
