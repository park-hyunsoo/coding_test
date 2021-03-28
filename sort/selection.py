array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 

for i in range(len(array)): 
    min_index = i 
    for j in range(i+1, len(array)): # 가장 작은 값의 위치를 찾음 
        if array[min_index] > array[j]: 
            min_index = j 
    array[i], array[min_index] = array[min_index], array[i] # 위치 변경 
    
print(array)
