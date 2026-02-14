power2 = [1,2,4,8,16,32,64,128]
N = int(input())
for i in power2:
    if N < i:
        print(i//2)
        exit()