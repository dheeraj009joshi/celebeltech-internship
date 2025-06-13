#!/bin/python3

import os

# Complete the solve function below.
def solve(s):
    out=[]
    print(s.split(" "))
    for i in s.split(" "):
        if len(i)>=1:
            if i[0].isalpha():
                out.append(i.title())
            else:
                out.append(i)
        else:
            out.append(i)
            
    a=" ".join(out)
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
