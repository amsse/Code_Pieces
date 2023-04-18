# Given the participants' score sheet for your University Sports Day, you are required to
# find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.
#
# Input Format:
# The first line contains n.
# The second line contains an array A[] of n integers each separated by a space.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
    # sorted() function returns a sorted list of the specified iterable object.
    # set() returns an unordered list constructed from the given iterable parameter (the variable "arr").
    # [-2] gets the second higher value from our list.
    # So, we sorted, than set a list, than asked for the second highest item on the list.