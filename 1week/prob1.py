N = int(input())
N_list = list(map(int, input().split()))
K = int(input())

def solution(index, N_list, K, ans, N):
    if index >= N:  # 종료 조건 수정
        return ans
    
    if N_list[index] < K:
        ans += 1
    
    return solution(index + 1, N_list, K, ans, N)  # N도 함께 전달

# 정답 출력
print(solution(0, N_list, K, 0, N)+1)
 