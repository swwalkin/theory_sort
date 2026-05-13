# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
m = 100
arr = [random.randint(1, m) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
C = [0 for _ in range(m+1)]
for i in arr:
    C[i] += 1

result = [0 for _ in range(arr_size)]
ind = 0
for i, k in enumerate(C):
    for _ in range(k):
        result[ind] = i
        ind += 1
######################################################################
# 결과 출력
print(time.time()-temp)
print(result)