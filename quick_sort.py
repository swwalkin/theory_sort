# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = quick_sort(arr)
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)