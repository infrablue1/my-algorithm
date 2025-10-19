

def radixSort(nums: list[int]) -> list[int]:
    n = len(nums)

    def countSort(exp: int):
        tmp = [0] * n
        count = [0] * 10
        nonlocal nums

        for num in nums:
            count[(num // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            tmp[count[index] - 1] = nums[i]
            count[index] -= 1

        nums = tmp

    maxNumber = max(nums)
    exp = 1
    while maxNumber // exp > 0:
        countSort(exp)
        exp *= 10

    return nums
