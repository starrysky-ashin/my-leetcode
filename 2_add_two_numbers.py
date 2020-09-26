"""
@File: 2_add_two_numbers.py
@Version: v0.0
@Author: jinxin@megvii.com
@Time: 2020-09-26 15:10
@Description: You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""


def num2linkedlist(num):
    num_str = str(num)[::-1]
    start = ListNode(0)
    node = start
    for i in num_str:
        node.next = ListNode(int(i))
        node = node.next
    return start.next


def linkedlist2num(l):
    num_str = ""
    while l:
        num_str += str(l.value)
        l = l.next
    return int(num_str[::-1])


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def add_two_numbers(l1, l2):
    """

    Args:
        l1 (ListNode): the first linked list
        l2 (ListNode): the second linked list

    Returns: ListNode

    """
    # We should get everything (variables) ready before starting the loop.
    # For example, creating a start listnode which points to the return node
    # is a useful trick.
    start = ListNode(0)
    node = start
    carry = 0
    s = 0
    while l1 or l2:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        s = val1 + val2 + carry
        carry = s // 10
        val = s % 10
        node.next = ListNode(val)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        node = node.next

    if carry == 1:
        node.next = ListNode(1)

    return start.next


if __name__ == "__main__":
    # test example 1
    num1 = 10
    num2 = 100

    l = add_two_numbers(num2linkedlist(num1), num2linkedlist(num2))
    print(linkedlist2num(l))
