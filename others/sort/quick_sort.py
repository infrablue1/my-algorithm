

def quickSort(nums: int) -> list[int]:

    def partition(left, right) -> int:
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    def quick(left: int, right: int) -> None:
        if left < right:
            pivotIndex = partition(left, right)
            quick(left, pivotIndex - 1)
            quick(pivotIndex + 1, right)

    quick(0, len(nums) - 1)
    return nums
