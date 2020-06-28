#!/bin/python3

from collections import Counter


# Complete the acmTeam function below.
def acmTeam(topic):
    topic = list(map(lambda n: int(n, 2), topic))
    all_couples = [bin(topic[m1] | topic[m2])[2:].count("1")
                   for m1 in range(len(topic))
                   for m2 in range(m1 + 1, len(topic))
                   ]
    topic_count = Counter(all_couples)
    max_subjects = -1 # This is the key in topic_count
    for t in topic_count:
        if t > max_subjects:
            max_subjects = t
    return [max_subjects, topic_count[max_subjects]]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
