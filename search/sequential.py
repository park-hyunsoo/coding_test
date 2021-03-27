def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
            
input_data = input().split() # 원소 개수, 찾을 단어 
n = int(input_data[0])
target = input_data[1]
array = input().split() # 목록

print(sequential_search(n, target, array))
