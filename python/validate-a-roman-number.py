import re

# Note: HackerRank test says "MMMM" is invalid, so "M*" must be replaced
# with "M{0,3}", but Wikipedia FR does not say so.
# https://fr.wikipedia.org/wiki/Num%C3%A9ration_romaine
regex_pattern = r"^M{0,3}(C{1,3}|CD|DC{0,3}|CM)?(X{1,3}|XL|LX{0,3}|XC)?(I{1,3}|IV|VI{0,3}|IX)?$" 	# Do not delete 'r'.


print(str(bool(re.match(regex_pattern, input()))))
