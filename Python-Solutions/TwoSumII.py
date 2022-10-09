def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if(sum == target):
            return [i+1, j+1]
        elif(sum > target):
            j -= 1
        else:
            i += 1
    return -1

numbersOne = [2,7,11,15]
numbersTwo = [2,3,4]
numbersThree = [-1,0]

print(twoSum(numbersOne, 9) == [1,2])
print(twoSum(numbersTwo, 6) == [1,3])
print(twoSum(numbersThree, -1) == [1,2])
