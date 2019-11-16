import re
phone = "(123) 456-7890"
bad = '[@:! )-.(]'
good = "[)-.( ]"

print(re.sub(bad, '', phone))
