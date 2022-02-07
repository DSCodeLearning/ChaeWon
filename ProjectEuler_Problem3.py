# 가장 큰 소인수 구하기

num = int(input("Enter number: "))

list = []

for i in range(1, num+1):
    if num % i == 0:
        list.append(i)

m = len(list) // 2
list = list[:m+1]

result_list = []

for m in list:
    for n in range(1, m+1):
        if m % n == 0:
            result_list.append(n)         
            
print(result_list)
