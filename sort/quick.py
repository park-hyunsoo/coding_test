array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개이면 종료
        return 
    pivot = start # 피벗, 시작요소
    left = start + 1
    right = end 
    
    while left <= right: # 왼쪽과 오른쪽이 교차 되면 종료
        # 큰 데이터 찾으면 종료
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 왼쪽 포인터는 같은 end에서 한칸 더 넘어가야 같은 경우 교체가 일어난다.
        
        # 작은 데이터 찾으면 종료
        while right > start and array[right] >= array[pivot]:
            right -= 1
      
        if left > right: # 교차 하는 경우 right가 왼쪽에 있으므로 위치를 변경
            array[right], array[pivot] = array[pivot], array[right]
            
        else:
            array[left], array[right] = array[right], array[left]
             
    quick_sort(array, start, right-1) # 왼쪽 리스트 재귀
    quick_sort(array, right+1, end) # 오른쪽 리스트 재귀

quick_sort(array, 0, len(array) -1)
print(array)

# 파이썬 특징을 사용한 퀵 정렬 수정
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗
    tail = array[1:] # 피벗을 제외한 요소
    
    left_side = [x for x in tail if x <= pivot] # 왼쪽
    right_side = [x for x in tail if x > pivot] # 오른쪽
    # 피벗 보다 작은 요소,
    # 피벗 보다 큰 요소를 별도로 구해서

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
