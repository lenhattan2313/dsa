from contextlib import nullcontext


class Solution:
    def __init__(self):
        self.heap = []

    def getLeftChildIndex(self, index):
        return index * 2 + 1

    def getRightChildIndex(self, index):
        return index * 2 + 2

    def getParentIndex(self, index):
        return (index - 1) // 2

    def swap(self, leftIndex, rightIndex):
        self.heap[leftIndex], self.heap[rightIndex] = self.heap[rightIndex], self.heap[leftIndex]

    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, index):
        while index > 0:
            parentIndex = self.getParentIndex(index)
            if self.heap[parentIndex] < self.heap[index]:
                self.swap(parentIndex, index)
                index = parentIndex
            else:
                break

    def extractMax(self):
        if self.heap == 1:
            return self.heap.pop()

        n = len(self.heap)
        value = self.heap[n - 1]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)

        return value

    def heapifyDown(self, index):
        n = len(self.heap)
        while self.getLeftChildIndex(index) < n:
            largestChildIndex = self.getLeftChildIndex(index)
            rightChildIndex = self.getRightChildIndex(index)
            if rightChildIndex < n and self.heap[largestChildIndex] < self.heap[rightChildIndex]:
                largestChildIndex = rightChildIndex

            if self.heap[index] < self.heap[largestChildIndex]:
                self.swap(largestChildIndex, index)
                index = largestChildIndex
            else:
                break




solution = Solution()
solution.insert(1)
solution.insert(2)
solution.insert(3)
solution.insert(7)
solution.insert(9)
solution.extractMax()

print(solution.heap)
