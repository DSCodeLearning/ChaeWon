# 가장 큰 소인수 구하기

num = int(input("Enter number: "))

list = []
i=2

while i <= num:
    if num % i == 0:
        list.append(i)
        num /= i 
    else: i+=1

print(list)
print(list[-1])
