n = int(input())

# 이진수 문자열 생성 함수
def generate_binary_numbers(length, current=""):
    if length == 0:
        return [current]
    return generate_binary_numbers(length - 1, current + "0") + generate_binary_numbers(length - 1, current + "1")

# 이진수 생성
binary_list = generate_binary_numbers(n)

def solution(binary_list, cnt):

    for binary in binary_list :
        # 인덱스 
        for i in range(n) :

            if i == n-1 :
                cnt +=1
                break
            
            # 0이 겹시면 break
            if binary[i] == '0' and binary[i+1] == '0' :
                break

    return cnt

ans = solution(binary_list, 0)

print(ans)


