def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        total = sum(arr)
        
        answer = N - 1  
        
        for k in range(1, N + 1):
            if total % k != 0:
                continue
            target = total // k
            cur = 0
            valid = True
            groups = 0
            for x in arr:
                cur += x
                if cur == target:
                    groups += 1
                    cur = 0
                elif cur > target:
                    valid = False
                    break
            if valid and groups == k:
                answer = min(answer, N - k)
        print(answer)

if __name__ == "__main__": # 터미널상에서 실행시킬 수 있는 파일로 만들어준다!
    solve()