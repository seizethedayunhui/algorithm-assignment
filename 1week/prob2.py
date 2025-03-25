N = int(input())
N_list = list(map(int, input().split()))
K = int(input())

# K와의 차이의 나타내는 gap 변수 초기화
gap = float('inf')
index = 0

def binary_search( begin, end, N_list, K, gap, index):

    # 인덱스 범위를 벗어나면 현재의 값 출력
    if begin > end :
        return index
    
    else : 
        # 이진 검색을 위한 중간 인덱스
        mid = ( begin + end ) // 2

        # gap 비교를 위한 mid 인덱스의 값과 K 값의 차이
        # 절댓값 처리를 위해 abs() 함수 사용
        current_gap = abs( K - N_list[mid] )

        # 만약 mid 인덱스의 값과 K의 차이가 이전의 gap 보다 작으면
        # 인덱스랑 gap 변수 값 변경
        if current_gap < gap :
            index = mid
            gap = current_gap
        
        # 만약 mid 인덱스 값과 K의 차이가 이전의 gap 보다 같은 경우
        elif current_gap == gap :
            # 해당 인덱스의 값과, 이전 최소의 차이를 보인 인덱스의 값의 값을 비교교
            if N_list[mid] < N_list[index] :
                index = mid

         # 이진 탐색 진행
         # 현재 정수가 K 보다 작은 경우 현재 정수보다 큰 값을 찾아야하는 경우
        if N_list[mid] < K:
            return binary_search(mid + 1, end, N_list, K, gap, index)
        # 현재 값이 K보다 크거나 같은 경우 현재 값보다 더 작은 값을 찾아야 함. 
        else:
            return binary_search(begin, mid - 1, N_list, K, gap, index)       
         
ans = binary_search( 0, N-1, N_list, K, gap, index)
print(N_list[ans])

