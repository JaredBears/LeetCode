#Given an integer array nums, move all 0's to the end of it while maintaining
#the relative order of the non-zero elements.
#
#Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    i = 0;
    count = 0;
    while count < len(nums):
        count += 1
        if nums[i] == 0:
            nums.append(nums.pop(i))
        else:
            i += 1

testOne = [0,1,0,3,12];
testTwo = [0]

moveZeroes(testOne)
moveZeroes(testTwo)

print(testOne==[1,3,12,0,0])
print(testTwo==[0])
