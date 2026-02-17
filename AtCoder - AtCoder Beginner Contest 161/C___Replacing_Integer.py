x, k = map(int,input().split())
first_step = abs(x) % k
second_step = abs(first_step - k)

print(min(first_step, second_step))