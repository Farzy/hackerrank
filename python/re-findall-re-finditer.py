import re

s = input()
res = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)
print(res)
if len(res) != 0:
    for voy in res:
        print(voy)
else:
    print("-1")
