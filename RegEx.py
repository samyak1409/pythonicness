# https://youtu.be/sa-TUpSx1JA -> just watch it again at 2x speed to clear all doubts in one go and relearn at the same time
# .
# abcd aa a
# 1234
# ./*+-
"""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
# http[s]?://(www.)?[a-z]+\.(com|gov)
# -> regex by me to match all those urls!
# (
# ? -> 0  or 1 time
# + -> 1 or more times
# {3} -> exactly 3 times
# )
# and
# [a-z]+\.(com|gov)
# try it by yourself by ctrl+f, and then using regex stuff!!
# imp note- we don't need to escape (\) special chars in char set [] and group ()

# https://youtu.be/K8L6KVGG-7o

import re

text_to_search_in = '''
.
abcd 
aa a
1234
./*+-
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

Mr Apple
Mrs Boy
Mr. Cat
Mrs. Dog
'''

pattern = re.compile(r'Mrs?.?\s[A-Z][a-z]+')  # raw string, i hope you known what and why it is
matches = pattern.finditer(text_to_search_in)
for match in matches:
    print(match)

# note that-> '^abc' -> match string starting with abc
# but-> '[^a-z]' -> will match anything but not lowercase a to z
