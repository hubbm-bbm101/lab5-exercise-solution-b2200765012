N=int(input("number N?"))
sum=0
average=0
for i in range(N+1):
    if i % 2 == 0:
        average+=i
for k in range(N+1):
    if k % 2 != 0:
        sum+=k
average = average//(N//2)
print("the sum of odd numbers to including N is " + str(sum))
print("the average of even numbers to including N is " + str(average))
