# 입력 1 : 5
# 입력 2 : R R R U D D
# 출력 : 3 4

n = int(input())
plans = input().split()

x, y = 1, 1

# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = {'L':0, 'R':1, 'U':2, 'D':3}

# 계획을 하나 꺼내서 
for plan in plans:
  nx = x + dx[move_types[plan]]
  ny = y + dy[move_types[plan]]  

  # 공간을 넘어가면 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)
