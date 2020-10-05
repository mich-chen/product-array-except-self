from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    products = []
    # setting all left and all right products from first and last index
    # as 1 because supposedly no elements in those regions
    left_p = 1
    right_p = 1

    for i in range(len(nums)):
        products.append(left_p)
        # update left_p to be product of all left elements
        left_p += nums[i]

    for i in range(len(nums) - 1, -1, -1):
        # update current 'all left products' to also multiply all right products
        products[i] *= right_p
        # update right_p to be product of all right elements
        right_p *= nums[i]

    return products


"""
Alternative solution:

def productExceptSelf(nums: List[int]) -> List[int]:

    products = []
    # initialize an array for all the left products
    left = [0] * len(nums)
    # initialize an array for all the right products
    right = [0] * len(nums)

    # iterate through to find all products of elements to the left of index i
    # all left from index 0 is 1 because no elements to the left
    left[0] = 1
    for i in range(1, len(nums)):
        # i-1 will give product of all the previous products from i
        left[i] = left[i - 1] * nums[i - 1]

    # iterate backwards from right for products of all elements right of index i
    # index len(nums) - 1 is 1 because no elements to the right of last index
    right[len(nums) - 1] = 1
    for i in range(len(nums) - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    # product would be all left products * all right products at index i
    for i in range(len(nums)):
        products.append(left[i] * right[i])
        # products[i] = left[i] * right[i]

    return products
"""


if __name__ == '__main__':

    print(productExceptSelf([1, 2, 3, 4])) # [24, 12, 8, 6]
    print(productExceptSelf([4, 5, 1, 8, 2])) # [80, 64, 320, 40, 160]
