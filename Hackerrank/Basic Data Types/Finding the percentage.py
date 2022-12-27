if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for i in student_marks[query_name]:
        # print(i)
        sum = sum + i
    # print(round(sum/3,2))
    print(f'{sum/3:.2f}')


#Cách 2


n = int(input())
student = {}
for i in range(n):
    name, *marks = input().split() # Giá trị đầu tiên sẽ lưu vào name, còn những giá trị còn lại sẽ lưu vào marks dưới dạng list string (*marks có nghĩa là cho phép nhập vào nhiều giá trị input)
    scores = list(map(float, marks)) # Chuyển list string nhập ở trên thành list giá trị float
    student[name] = scores 
nameProvided = input()
print(f'{sum(student[nameProvided])/3:.2f}')
# f-string f'{value: .2f}' 