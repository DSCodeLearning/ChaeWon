# 가장 큰 소인수 구하기
# [220101] try1

num = int(input("Enter number: "))

list1 = []
list2 = []

for i in range(2, num):
    rem = num % i
    if rem == 0:
        list1.append(i)
  
for quo in list1:
    result = list1[m] % quo
    if result != 0:
        list2.append(quo)
        m += -1
        if m < 0:
            break
    print(list2)