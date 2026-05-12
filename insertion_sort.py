# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
for i in range(1, arr_size):
    key = arr[i]
    k = i - 1
    while k >= 0 and arr[k] > key:
        arr[k+1] = arr[k]
        k -= 1
    arr[k+1] = key
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)