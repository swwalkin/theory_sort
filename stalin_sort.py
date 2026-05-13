# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
i = 0
for _ in range(arr_size-1):
    if arr[i] > arr[i+1]:
        del arr[i+1]
    else:
        i += 1
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)
