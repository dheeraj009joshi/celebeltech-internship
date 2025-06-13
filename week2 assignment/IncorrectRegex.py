# done with using python2 

import re
for _ in range(int(raw_input())):
    try:
        re.compile(raw_input().strip())
        print(True)
    except re.error:
        print(False)