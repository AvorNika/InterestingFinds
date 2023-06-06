user_nums = [int(num) for num in input().split()]


def containsDuplicate(nums):
    new_nums = set(nums)
    return len(nums) != len(new_nums)


print(containsDuplicate(user_nums))
