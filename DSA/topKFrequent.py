from collections import Counter
import heapq


def top_k_frequent(arr, k):
    counter = Counter(arr)
    heap = []
    for key, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap,(freq, key))
        else:
            heapq.heappushpop(heap, (freq, key))
    return [h[1] for h in heap]

# Time complexity: O(n * log(k))
# Space complexity: O(n)


def top_k(arr, k):
    n = len(arr)
    counter = Counter(arr)
    bucket = [0] * (n + 1) #[0, 0, 0 ,0] 0 time

    for key, freq in counter.items():
        if bucket[freq] == 0:
            bucket[freq] = [key]
        else:
            bucket[freq].append(key)

    result = []
    for i in range(n, -1, -1):
        if bucket[i]:
            result.extend(bucket[i])
        if len(result) == k:
            break

    return

# Time complexity: O(n)
# Space complexity: O(n)
print(top_k([1, 1, 2, 2, 2, 3,3, 3], 2))
