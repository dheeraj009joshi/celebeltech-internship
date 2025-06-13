def average(array):
    sum=0
    new_arr=set(arr)
    for i in new_arr:
        sum+=i
    avg=sum/len(new_arr)
    rounded=round(avg,3)
    return rounded

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)