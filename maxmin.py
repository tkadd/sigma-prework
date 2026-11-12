def maxmin(nums) -> list:
    minimum, maximum = float("inf"), float("-inf")

    for num in nums:
        if num < minimum: minimum = num
        if num > maximum: maximum = num

    return [minimum, maximum]

if __name__ == "__main__":
    nums = [2, 4, 1, 0, 2, -1]
    print(maxmin(nums))
