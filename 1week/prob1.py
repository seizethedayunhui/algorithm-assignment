# 억지스러운 문제 ????.????
# 파이썬으로 푼다면, 일단 전체 배열을 들고다니지는 말고 .......... 부분 배열로 잘라서 들고가야한다??????

N = int(input())
N_list = list(map(int, input().split()))
K = int(input())


def solution(index, N_list, K, ans, N):
    # 종료 조건 수정, index > N 으로 설정하면 range out of index 발생 가능
    # 범위를 벗어나면 바로 값 반환
    if index >= N:  
        return ans
    
    # 현재 인덱스의 값이 임의의 정수 K 보다 작으면 ans += 1
    if N_list[index] < K:
        ans += 1
    
    # 반복문 대신에 index +1 해주는 recursion
    return solution(index + 1, N_list, K, ans, N)  # N도 함께 전달

# 정답 출력
print(solution(0, N_list, K, 0, N)+1)
