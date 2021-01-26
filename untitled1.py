import random
ans = random.randint(1,10)
count=0
while True:
    guess = int(input("guess number?"))
    if ans==guess:
        print("right")
        count+=1
        print(count)
        break
    elif ans < guess:
        print("lower")
    else:
        print("higher")
    count+=1
            
