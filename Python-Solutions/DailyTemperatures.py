#Given an array of integers temperatures represents the daily temperatures,
#return an array answer such that answer[i] is the number of days you have to
#wait after the ith day to get a warmer temperature. If there is no future day
#for which this is possible, keep answer[i] == 0 instead.

def dailyTemperaturesBruteForce(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    i = 0
    j = 1
    while i < len(temperatures) - 1:
        if(j > len(temperatures) - 1):
            answers.append(0)
            i += 1
            j = i + 1
        elif temperatures[j] > temperatures[i]:
            answers.append(j - i)
            i += 1
            j = i + 1
        else:
            j += 1
    answers.append(0)
    return answers

def dailyTemperaturesStack(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    answers = [0] * len(temperatures)
    stack = []
    i = 0
    while i < len(temperatures):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev = stack.pop()
            answers[prev] = (i - prev)
        stack.append(i)
        i += 1
    return answers

temperaturesOne = [73,74,75,71,69,72,76,73]
testOne = [1,1,4,2,1,1,0,0]

temperaturesTwo = [30,40,50,60]
testTwo = [1,1,1,0]

temperaturesThree = [30,60,90]
testThree = [1,1,0]

print(dailyTemperaturesStack(temperaturesOne) == testOne)
print(dailyTemperaturesStack(temperaturesTwo) == testTwo)
print(dailyTemperaturesStack(temperaturesThree) == testThree)
