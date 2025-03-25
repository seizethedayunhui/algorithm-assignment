# 입력 받기
with open("input.txt", "r") as file:
    lines = file.readlines()

N = int(lines[0].strip())  # 아이템의 개수
W = int(lines[1].strip())  # 총량량
W_list = list(map(int, lines[2].split()))  # 아이템들의 무게
V_list = list(map(int, lines[3].split()))   # 아이템들의 가격

def solution(index, W, value, currentV) :
    # 종료 조건: 모든 물건을 처리한 경우 (index가 N 이상인 경우)
    if index >= N :
        # 현재까지 구한 값과 기존 값 중 최대값을 선택
        value = max(value, currentV)
        return value  # 종료 시 값을 반환

    # 현재 물건을 넣을 수 있는 경우 (무게가 초과되지 않는 경우)
    currentW = W - W_list[index]

    # 물건을 선택하는 경우
    if currentW >= 0 :
        value = solution(index + 1, W - W_list[index], value, currentV + V_list[index])
    
    # 물건을 선택하지 않는 경우
    value = solution(index + 1, W, value, currentV)

    return value  # 최대값 반환

value = float('-inf')
ans = solution(0, W, value, 0)

print(ans)