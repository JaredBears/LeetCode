def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 1
    while i < len(nums):
        nums[i] += nums[i-1]
        i += 1
    return nums

testOne = [1,2,3,4]
testTwo = [1,1,1,1,1]
testThree = [3,1,2,10,1]

print(runningSum(testOne) == [1,3,6,10])
print(runningSum(testTwo) == [1,2,3,4,5])
print(runningSum(testThree) == [3,4,6,16,17])
