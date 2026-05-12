# 기본설정
import random, time
######################################################################
# 변수
arr_size = 1000
arr = [random.randint(1, 100) for _ in range(arr_size)]
######################################################################
# 정렬
temp = time.time()
def merge_sort(ar):
    if len(ar) <= 1:
        return ar

    left = merge_sort(ar[:len(ar)//2])
    right = merge_sort(ar[len(ar)//2:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = merge_sort(arr)
######################################################################
# 결과 출력
print(time.time()-temp)
print(arr)
