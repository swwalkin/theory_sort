# 기본설정
import random, time
######################################################################
# 변수
arr_size = 10
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
while True:
    check = False
    for i in range(arr_size-1):
        if arr[i] > arr[i+1]:
            random.shuffle(arr)
            check = True
            break
    if check: continue
    break
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)