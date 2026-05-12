# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
for i in range(arr_size):
    for j in range(arr_size-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)