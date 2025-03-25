import sys
# 파이썬 재귀의 깊이 증가시킴
sys.setrecursionlimit(10**6)  

# 입력 받음. 
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N) ]
K = int(input())


# 동 남 서 북
dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

# 범위 확인 함수 
def in_range(x, y) :
    return 0<= x < N and 0<= y < N

# 미로찾기 순환함수 작성
def solution( x, y, dx, dy, arr, cnt) :

    # 끝점에 도착하면, 길이 확인후 종료
    if x == N - 1 and y == N - 1 :
        if cnt <= K :
            return 1
        else :
            return 0
        
    ans = 0

    for i in range(4) :

        nx = x + dx[i]
        ny = y + dy[i]

        # 움직일 수 있는 범위인지 확인.
        if in_range(nx, ny) and arr[nx][ny] == 0 :

            # 이렇게 표시를 안해주면 갔던 곳을 계속 방문할 수도 있음.
            arr[nx][ny] = 1
            # 리턴해주는 값을 ans에 누적해줌. 
            ans += solution( nx, ny, dx, dy, arr, cnt + 1)
            # 백트래킹으로 원래 값으로 돌려놓음.
            arr[nx][ny] = 0
    
    # 아무조건에도 해당하지 않으면 그냥 종료
    return ans

arr[0][0]=1
print(solution(0, 0, dx, dy, arr, 0))
