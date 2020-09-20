"""
@File: 1_two_sum.py
@Version: v0.0
@Author: jinxin@megvii.com
@Time: 2020-09-19 22:06
@Description: 
Given an array of integers (nums) and an integer (target), return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    """Find the indices of the two numbers in a list that add up to the target
    This implementation uses the 'in' statement for iterable object and the index method for list object.

    Args:
        nums (List[int]): a list of integers
        target (int): the target integer

    Returns: List[int]

    """
    for i in range(len(nums)):
        if target-nums[i] in nums[i+1:]:
            return [i, i+1+nums[i+1:].index(target-nums[i])]

def two_sum_by_hashmap(nums, target):
    """Find the indices of the two numbers in a list that add up to the target
    This implementation uses the dict object as hashmap to reduce the query time.

    Args:
        nums (List[int]): a list of integers
        target (int): the target integer

    Returns: List[int]

    """
    hashmap = dict()
    for i in range(len(nums)):
        if target-nums[i] in hashmap:
            return [hashmap[target-nums[i]], i]
        else:
            hashmap[nums[i]] = i


if __name__ == "__main__":
    # test example
    nums = [2, 7, 11, 5]
    target = 18
    print(two_sum(nums, target))

    # test time
    # from timeit import Timer
    # exe_num = 20000000
    # func_name = "two_sum_by_hashmap"
    # t1 = Timer("%s(nums, target)" % func_name,
    #         "from __main__ import %s; nums=%s; target=%s" % (func_name, nums, target))
    # print("Executing func %s %d times costs %.3f second!" % (func_name, exe_num, t1.timeit(number=exe_num)))
