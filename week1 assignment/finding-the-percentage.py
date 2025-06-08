if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for k,v in student_marks.items():
        if k == query_name:
            total = 0
            for i in v:
                total += i
            average = total/len(scores)
    print("{:.2f}".format(average))
