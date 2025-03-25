import sys

# 상하좌우 방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 미로 내의 위치가 유효한지 확인하는 함수
def is_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

# DFS 백트래킹을 사용하여 최소 휴식 횟수를 찾는 함수
def dfs(maze, visited, x, y, N, K, rest, min_rest):
    # 출구 도착 시 최소 휴식 횟수 갱신
    if x == N - 1 and y == N - 1:
        return min(min_rest, rest)

    visited[x][y] = True  # 현재 위치 방문 처리

    # 현재 위치에서 일직선으로 최대 K칸까지 이동
    for d in range(4):
        for k in range(1, K + 1):
            nx, ny = x + k * dx[d], y + k * dy[d]

            # 범위 확인 + 방문할 수 있는지 확인
            if is_range(nx, ny, N) and not visited[nx][ny] and maze[nx][ny] == 0:
                min_rest = min(min_rest, dfs(maze, visited, nx, ny, N, K, rest + 1, min_rest))
            else:
                # 벽을 만나거나 범위를 벗어나면 더 이상 진행 불가 -> break
                break  

    visited[x][y] = False  # 백트래킹
    return min_rest  # 수정: 최솟값 반환

# 입력 받기
with open("maze.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())  # 미로 크기
maze = [list(map(int, lines[i + 1].split())) for i in range(N)]  # 미로 데이터
K = int(lines[N + 1].strip())  # 최대 이동 가능 칸

visited = [[False] * N for _ in range(N)]  # 방문 체크 배열
min_rest = float('inf')  # 최소 휴식 횟수 저장

# 최소 휴식 횟수 찾기
result = dfs(maze, visited, 0, 0, N, K, 0, min_rest)

# 도달할 수 없는 경우 -1 반환
print(result if result != float('inf') else -1)
