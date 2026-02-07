n, k = map(int, input().split())
count = 0
for i in range(n):
    temp = i+1
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    temp5 = 0
    if temp >= 100000:
        temp5 = temp//100000
        temp = temp%100000
    if temp >= 10000:
        temp4 = temp//10000
        temp = temp%10000
    if temp >= 1000:
        temp3 = temp//1000
        temp = temp%1000
    if temp >= 100:
        temp2 = temp//100
        temp = temp%100
    if temp >= 10:
        temp1 = temp//10
        temp = temp%10
    ans = temp + temp1 + temp2 + temp3 + temp4 + temp5
    if ans == k:
        count += 1
print(count)