def find_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if isinstance(nums[i], str) or nums[i] < 0:
            return False
        if nums[i] == nums[i - 1]:
            return nums[i]
    return False

    # return len(nums) != len(set(nums))
    # nums.sort()
    # duplicate = {}
    # for num in nums:
    #     if num in duplicate:
    #         return num
    #     duplicate[num] = 1
