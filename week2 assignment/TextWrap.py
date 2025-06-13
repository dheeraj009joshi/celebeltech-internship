import textwrap

def wrap(string, max_width):
    
    n = list(string)
    k = len(n) - 1
    j = 0
    m = []
    while(k != 0):
        t = ""
        for i in range(1, max_width+1):
            if j < len(n):
              t += n[j]
              j += 1
            
        k -= 1
        m.append(t)
        if j == len(n):
            break
    f = ""
    for i in range(len(m)):
        if(i == len(m)-1):
            f += m[i]
            break
        f += m[i] + "\n"
            
    return f