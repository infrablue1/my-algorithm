

def heapSort(nums: int) -> list[int]:

    def maxHeapify(start: int, end: int):
        parent = start
        child = parent * 2 + 1
        while child <= end:
            if child + 1 <= end and nums[child + 1] > nums[child]:
                child += 1
            if nums[parent] > nums[child]:
                return
            nums[parent], nums[child] = nums[child], nums[parent]
            parent = child
            child = 2 * parent + 1

    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(i, n - 1)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        maxHeapify(0, i - 1)

    return nums
