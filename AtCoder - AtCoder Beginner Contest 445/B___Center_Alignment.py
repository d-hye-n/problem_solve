N = int(input())
words = []
for i in range(N):
    words.append(input())

k = 1
for i in range(N):
    k = max(k,len(words[i]))

for i in range(N):
    words[i] = words[i].center(k,'.')
print(*words,sep='\n')