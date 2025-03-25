# 입력 받기
with open("input9.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())  # 선수 
arr = [list(map(int, lines[i + 1].split())) for i in range(N)] 
K = int(lines[-1].strip())  # 선택하는 사람의 수
check_list = list()

# 선택된 선수들의 능력치의 합 구하는 함수
def value_sum(check_list, arr):

    current_value = 0

    for i in check_list:
        for j in check_list:
            current_value += arr[i][j]

    return current_value


def solution(index, N, K, check_list, arr, value):

    if K == 0:
        # 현재 check_list에 있는 값 구하기기
        current_value= value_sum(check_list, arr)
        value = max(value, current_value)
        return value
    
    # 인덱스를 벗어나는 경우 value값 반환. -> value가 음수인 경우이 부분이 없다면 다른 값이 나올 수 있음. 
    if index >= N :
        return value

    # 현재 선수를 포함하는 경우
    check_list.append(index)
    value = solution(index+1, N, K-1, check_list, arr, value)

    # 현재 선수를 포함하지 않는 경우
    check_list.pop()
    value = solution(index+1, N, K, check_list, arr, value)

    return value

value = float('-inf')
ans = solution(0, N, K, check_list, arr, value)

print(ans)