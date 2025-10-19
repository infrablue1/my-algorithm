

def mergeSort(nums: int) -> list[int]:

    def merge(left: int, mid: int, right: int):
        leftArray = nums[left:mid + 1]
        rightArray = nums[mid + 1:right+1]
        a, b = 0, 0
        i = left

        for i in range(left, right + 1):
            if a < len(leftArray) and b < len(rightArray):
                if leftArray[a] < rightArray[b]:
                    nums[i] = leftArray[a]
                    a += 1
                else:
                    nums[i] = rightArray[b]
                    b += 1
            else:
                if a < len(leftArray):
                    nums[i] = leftArray[a]
                    a += 1
                else:
                    nums[i] = rightArray[b]
                    b += 1

    def _mergeSort(left: int, right: int):
        if left < right:
            mid = left + (right - left) // 2
            _mergeSort(left, mid)
            _mergeSort(mid + 1, right)
            merge(left, mid, right)

    _mergeSort(0, len(nums) - 1)
    return nums
