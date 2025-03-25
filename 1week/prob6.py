n = int(input())
num_list = list( map(int, input().split()) )

def solution(index, n, num_list) :

    # 끝에 도착하면 True 반환
    if index == n-1 :
        return True
    
    # 이동
    for i in range(1, num_list[index]+1 ) :
        d = index + i 

        # 인덱스 범위를 벗어나거나, 0인 경우 이동할 수 없으므로 continue
        if d >= n or num_list[d] == 0 :
            continue
        
        # 반환값 확인 후 True 면 True 반환 후 종료. 
        if solution( index+i, n, num_list) :
            return True
    # True를 반환한 적이 없으면, False 반환  
    return False


if solution(0, n, num_list) :
    print("Yes")
else :
    print("No")       