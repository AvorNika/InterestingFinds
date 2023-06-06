user_nums = [int(num) for num in input().split()]


def missingNumber(nums):
    n = len(nums)
    result_nums = {int(i) for i in range(n+1)}
    new_nums = set(nums)
    return sum(result_nums - new_nums)


print(type(missingNumber(user_nums)))
