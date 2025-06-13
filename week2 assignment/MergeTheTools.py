import textwrap
def merge_the_tools(string, k):
    # your code goes here
    chunks = textwrap.wrap(string, k)
    for a in chunks:
        print(''.join(list(set(a))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)