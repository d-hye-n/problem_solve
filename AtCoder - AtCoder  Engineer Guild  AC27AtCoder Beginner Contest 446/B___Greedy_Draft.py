import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    juices = [1]*(M+1)
    ans = [0]*N
    for i in range(N):
        L = int(input())
        hope = list(map(int, input().split()))
        for x in hope:
            if juices[x]:
                juices[x] = 0
                ans[i] = x
                break
    print(*ans,sep='\n')

if __name__ == '__main__':
    main()