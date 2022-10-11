# Given an integer array nums, return true if there exists a triple of
# indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no
# such indices exists, return false.

#Naive solution works, but will fail due to time constraints
def increasingTripletNaive(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            k = j + 1
            while k < len(nums):
                if(nums[i] < nums[j] and nums[j] < nums[k]):
                    return True
                k += 1
            j += 1
        i += 1
    return False;

# Better, and accepted: only returns true in a case where N is greater than the
# second value, which is greater than the first value. Pay attention to the
# less than/equals

def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    first = float('inf')
    second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


testOne = [1,2,3,4,5]
testTwo = [5,4,3,2,1]
testThree = [2,1,5,0,4,6]

print(increasingTriplet(testOne) == True)
print(increasingTriplet(testTwo) == False)
print(increasingTriplet(testThree) == True)
