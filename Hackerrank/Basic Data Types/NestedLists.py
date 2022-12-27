n = int(input())
data = []
score_list = []
student = []
for i in range(n):
    name = input()
    score = float(input())
    score_list.append(score)
    data.append([name,score])

score_list.sort()
secondLowestGrade = [i for i in score_list if i != min(score_list)]
for i in data:
    if i[1] == secondLowestGrade[0]:
        student.append(i[0])
student.sort()
print(*student,sep = "\n") 
# '*' là in ra giá trị của list, 
# 'sep' là chỉ định từng giá trị phân tách nhau bằng kí tự gì