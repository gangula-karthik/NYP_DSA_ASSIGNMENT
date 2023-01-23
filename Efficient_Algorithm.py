# NAME: GANGULA KARTHIK 
# ADMISSION_NO: 223715Y
# TUTORIAL_GROUP: BA2202
############################################################################################################
# 2 pointer method
# Using a while loop is much faster and more memory efficient in this case than using recursion as the function does not need to keep track of multiple recursive calls on the call stack.

# O(n) time complexity
# O(1) space complexity


def two_number_sum(seq: int, z: int) -> str:
    """
    Finds two numbers in the given sequence whose sum equals the target number.

    Parameters:
    seq (list[int]): The sequence of numbers to search.
    z (int): The target sum.

    Returns:
    str: A string containing the values of the two numbers, and a boolean indicating whether their sum equals the target. The values of the two numbers are represented as "x" and "y". If the two numbers are not found, they are represented as "not found".
    """
    # initializing high and low pointers
    low = 0
    high = len(seq) - 1
    # doing a while loop until pointers meet each other
    while low < high:
        curr_sum = seq[low] + seq[high]
        # If sum is equal to target, return the two numbers
        if curr_sum == z: 
            return f"x = {seq[low]}\ny = {seq[high]}\n{seq[low] + seq[high] == z}"
        # If sum is less than target, move the low pointer up
        elif curr_sum < z:
            low += 1
        # If sum is more than target, move the high pointer down
        else: 
            high -= 1
    # If pointers meet each other and no sum is found, return not found
    return f"x = not found\ny = not found\n{False}"
