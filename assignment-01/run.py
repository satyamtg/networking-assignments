import matplotlib.pyplot as plt
import numpy as np


def getMaxLengthOConsecutiveNoInBinaryArray(arr, n, no):
    count = 0
    result = 0
    for i in range(0, n):
        if (arr[i] == no):
            count = 0
        else:
            count += 1
            result = max(result, count)
    return result


def findAutoCorrelation(arr, n):
    transformedArr = arr
    autoCorrelationArray = []
    for shift in range(len(arr)):
        a = 0
        d = 0
        for i in range(len(arr)):
            if(arr[i] == transformedArr[i]):
                a += 1
            else:
                d += 1
        autoCorrelationArray.append(abs((a-d)/n))
        transformedArr = (transformedArr[len(
            transformedArr) - 1:len(transformedArr)] + transformedArr[0:len(transformedArr) - 1])
    return(autoCorrelationArray)


r = 3

seedBit1 = 1
seedBit2 = 0
seedBit3 = 1

maxLength = int(input("Enter the max length of sequence: "))

resultantArr = []

for i in range(maxLength):
    tempBit1 = seedBit3
    tempBit2 = seedBit1
    seedBit3 = seedBit2
    seedBit2 = seedBit1
    seedBit1 = tempBit1 ^ tempBit2
    resultantArr.append(seedBit3)

print(resultantArr)

print("Checking the properties...")

period = 2 ** r - 1
print("Period is " + str(period))
periodWiseList = [resultantArr[i * period:(i + 1) * period]
                  for i in range((len(resultantArr) + period - 1) // period)]
if(len(periodWiseList[-1]) < period):
    periodWiseList.pop(-1)
errorOccurred = [0]*8
for period in periodWiseList:
    noOfOnes = 0
    noOfZeroes = 0

    for i in period:
        if(i == 1):
            noOfOnes += 1
        elif(i == 0):
            noOfZeroes += 1
        else:
            print("Error Occured while counting number of ones and zeroes")

    if(noOfOnes != 2 ** (r - 1)):
        errorOccurred[0] = 1
    if(noOfZeroes != 2 ** (r-1) - 1):
        errorOccurred[1] = 1
    if(getMaxLengthOConsecutiveNoInBinaryArray(period, len(period), 0) != r):
        errorOccurred[2] = 1
    if(getMaxLengthOConsecutiveNoInBinaryArray(period, len(period), 1) == r):
        errorOccurred[3] = 1

if(errorOccurred[0] == 0):
    print("Number of ones in a period is 2** (r - 1)")
if(errorOccurred[1] == 0):
    print("Number of zeroes in a period is 2**(r-1) - 1")
if(errorOccurred[2] == 0):
    print("No of consecutive ones in a period is equal to r")
if(errorOccurred[3] == 0):
    print("Sequence does not have any occurrence of total number of r zeroes in succession")

autoCorrelationArr = findAutoCorrelation(periodWiseList[0], 3)

print(autoCorrelationArr)

noOfPeriods = 5

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
y = np.tile(autoCorrelationArr, noOfPeriods)
x = range(len(y))

ax.bar(x, y)
plt.show()
