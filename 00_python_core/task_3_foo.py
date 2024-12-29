from typing import List


def foo(nums: List[int]) -> List[int]:
    n = len(nums)
    if n==0:
        return []
    
    # Step 1: Create a result list initialized with 1's
    result = [1] * n
    
    # Step 2: Compute left products and store them in the result list
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    
    # Step 3: Compute right products and multiply them with the result list
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result
