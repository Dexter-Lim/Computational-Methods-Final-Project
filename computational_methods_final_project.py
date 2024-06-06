import \
    matplotlib.pyplot as plt  # <------------If ur are in a Py virtual environment make sure you install these packages, or install then globally if ur not
import numpy as np

#Chapter 1

#This function will convert binary values that are right of the decimal point to base-10, I can use int(value, 2) to convert integer values to base 10
def decimalBinaryToBaseTen(Binary):
    value = 0
    for index, Units in enumerate(Binary):
        value = value + int(Units) * 2 ** ((index + 1) * (-1))
    return value


data = open("BinaryData_Chapter1.txt", "r")

#Cleaning up data and organizing it.

biList = []
for line in data:
    line = line.strip()  #Remove whitespace from beginning and end of line
    line = line.replace(" ", "")  # Removes the spaces between each number
    biList.append(line)  #Adds new clean data to biList

#Indexing the floating point binary data from biList and converting it base 10, then placing it in baseTenList


baseTenList = []
for line in biList:  #This will iterate for every float point binary number

    sign = int(line[0])  #Checks the sign of the mantissa
    if sign == 0:
        sign = 1
    else:
        sign = -1

    exp_sign = int(line[1])  #Checks the sign of the exponent
    if exp_sign == 0:
        exp_sign = 1
    else:
        exp_sign = -1

    expMag = int(line[2:5], 2)  #Finds the integer value of the exponent
    mantissa = line[5:10]

    # We need to move the decimal point expMag times to the right or left
    if exp_sign == 1:  # This will run if the exponent is positive
        if expMag <= len(
                mantissa):  # If the length of the exponent is less then the length of the mantissa we need to add a "." in the middle of the mantissa
            mantissa = "1" + mantissa[0:expMag] + "." + mantissa[expMag:len(mantissa) + 1]
        else:
            # noinspection PyTypeChecker
            for i in len(
                    expMag):  # If the length of the exponent is greater than the mantissa we need to add zeros to the end on the mantissa
                mantissa = mantissa + "0"
            mantissa = "1" + mantissa
    else:
        for i in len(expMag):
            mantissa = "0" + mantissa

    valueLeftOfPoint = ""
    valueRightOfPoint = ""
    for index, value in enumerate(
            mantissa):  # This will iterate for every character in the mantissa including the decimal point
        if value != '.':
            valueLeftOfPoint = valueLeftOfPoint + value  # This will assign every value left of the decimal point to its own variable
        else:
            valueRightOfPoint = mantissa[index + 1:len(
                mantissa)]  # This will assign every value right of the decimal point to its own variable
            break
    # This will convert and sum the integer binary and the fractional binary and add them to the list baseTenList
    baseTenList.append(sign * (int(valueLeftOfPoint, 2) + float(decimalBinaryToBaseTen(valueRightOfPoint))))


print("Floating Point Binary --> Base-10")
for row1, row2 in zip(baseTenList,biList):
    print(f'{row2} --> {row1}')

plt.figure(1)
x = np.arange(0, 20.1, 0.1)
y = x ** 2 * np.exp(-1 / 2 * x)
plt.scatter(np.arange(0.1, 0.9, 0.1), baseTenList)
plt.xlabel('Time(ms)')
plt.ylabel("Charge(mC)")
plt.show()

TrueCharge = [24.89, 14.32, 5.16, 14.32, 22.13, 8.54, 4.32, 1.11]
ApproximateCharge = baseTenList


def relative_true_error(TrueValue, ApproximateValue):
    RteList = []
    for index, value in enumerate(TrueValue):
        RteList.append(((value - ApproximateValue[index]) / value) * 100)
    return RteList


RteList = relative_true_error(TrueCharge, ApproximateCharge)
plt.figure(2)
plt.plot(np.arange(0.1, 0.9, 0.1), RteList)
plt.xlabel('Time(ms)')
plt.ylabel("Relative True Error(%)")
plt.show()

#Chapter 2

#Forward Difference formula: f'(x) = (f(x+h)-f(x)/h
#Backward Difference formula: f'(x) = (f(x) - f(x-h))/h
#Central Difference formula: f'(x) = (f(x+h)-f(x-h))/2h
fPrime = []
for index, value in enumerate(baseTenList):
    if index == 0:
        fPrime.append((baseTenList[1]-value)/0.1)
    elif index != 0 and index != len(baseTenList) - 1:
        fPrime.append((baseTenList[index + 1]-baseTenList[index - 1])/0.1)
    else:
        fPrime.append((value-baseTenList[index - 1])/0.1)

print(fPrime)



