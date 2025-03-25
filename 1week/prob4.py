# 미로의 크기
N = int(input())
# 격자의 입력
arr = [ list(map(int, input().split())) for _ in range(N) ]
# 폭탄의 개수
K = int(input())

# 범위 확인 함수
def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N


def solution( x, y, cnt, K, N, arr) :

    # K번 초과하는 경우 죽음
    if cnt > K :
        return False
    
    # 도착지점에 도착한 경우
    if ( x == N-1 ) and ( y == N-1 ) :
        return True
    
    # 동 남 서 북
    dx = [ 0, 1, 0, -1 ]
    dy = [ 1, 0, -1, 0 ]

    for i in range(4) :
        
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크
        if (in_range(nx, ny) and arr[nx][ny] >= 0 ) :
            # 벽인 경우
            if ( arr[nx][ny] == 1 ) :
                continue
            # 폭탄인 경우
            elif (arr[nx][ny] == 2 ) :
                arr[nx][ny] -= 1
                # 충돌 cnt + 1
                # 반환값을 확인해서 True가 반환되면 즉시 반환해야함. 
                if solution( nx, ny, cnt+1, K, N, arr) :
                    return True
            else :
                arr[nx][ny] -= 1
                if solution( nx, ny, cnt, K, N, arr) :
                    return True
            
            # 원래 값 복원 
            arr[nx][ny] += 1
    # True로 반환되는 값이 없으면 False 반환 
    return False
   
if solution(0, 0, 0, K, N, arr) :
    print("Yes")
else :
    print("No")

    