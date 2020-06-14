import re

regex_pattern = r"^[a-zA-Z][\w_-]*@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$"


def fun(s):
    return re.search(regex_pattern, s) is not None


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
