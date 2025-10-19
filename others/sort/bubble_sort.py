

def bubbleSort(nums: int) -> list[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums
