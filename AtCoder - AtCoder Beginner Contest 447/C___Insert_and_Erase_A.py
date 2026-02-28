S = input()
T = input()

def sol(s):
    no_A = []
    section = []
    i = 0
    n = len(s)
    cnt = 0
    while i < n and s[i] == "A":
        cnt += 1
        i += 1
    section.append(cnt)

    while i < n:
        if s[i] != 'A':
            no_A.append(s[i])
            i += 1
            cnt = 0
            while i < n and s[i] == 'A':
                cnt += 1
                i += 1
            section.append(cnt)
        else:
            i += 1
    return no_A, section

no_A_S, section_S = sol(S)
no_A_T, section_T = sol(T)

if no_A_S != no_A_T:
    print(-1)
else:
    print(sum(abs(a-b) for a, b in zip(section_S, section_T)))