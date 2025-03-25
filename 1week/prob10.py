# 입력 받기
with open("input10.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())  # 물건의 개수수 
arr = [list(map(int, lines[i + 1].split())) for i in range(N)] 
W = int(lines[-1].strip())  # 부피의 총량 제한

check_list = list()

# 가져가는 물건의 합- 가져가지 않는 물건의 합.
def value_sum( check_list, arr, N) :

    include_sum = 0 
    not_include_sum = 0
    current_value = 0

    # 가져가지 않는 물건의 폐기비용 합 
    for i in range(N) :
        if i not in check_list: 
            not_include_sum += arr[i][2]
    
    # 가져가는 물건의 가격 합
    for i in check_list :    
        include_sum += arr[i][1]

    # 가져가는 물건의 가격의 합 - 가져가지 않는 물건의 폐기비용 합합
    current_value = include_sum - not_include_sum

    return current_value

def solution(index, W, check_list, arr, value):

    # value 값 구하기
    if index >= N :
        # 최대값 구하기
        current_value = value_sum(check_list, arr, N)
        value = max(value, current_value)
        return value

    # 가져가는 물건의 가격의 합에 가져가지 않을 물건의 페기 비용을 뺀 값의 최대값.
    # 현재 물건을 포함하는 경우
    current_weight = arr[index][0]
    if W - current_weight >= 0 :
        check_list.append(index)
        value = solution(index + 1, W - current_weight, check_list, arr, value)
        check_list.pop()

    # 현재 물건을 포함하지 않는 경우
    value = solution(index + 1, W, check_list, arr, value)

    return value

value = float('-inf')
ans = solution(0, W, check_list, arr, value)
print(ans)