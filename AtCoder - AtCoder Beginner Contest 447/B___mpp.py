strings = list(input())
max_num = max(strings.count(s) for s in set(strings))
strings = [s for s in strings if strings.count(s) != max_num]

print(*strings,sep='')