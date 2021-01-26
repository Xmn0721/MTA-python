score_list=[]
num = int(input("number?"))
for i in range(num):
    score=int(input("score?"))
    score_list.append(score)
score_list.sort()
print("highest",score_list[-1])
print("lowest",score_list[0])
print(score_list)