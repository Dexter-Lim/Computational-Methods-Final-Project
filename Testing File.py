data = open("Data_Chapter3.txt", "r")

#Cleaning up data and organizing it.

timeList = []
currentList = []
for line in data:
    line = line.strip().split('\t')
    timeList.append(float(line[0]))
    currentList.append(float(line[1]))
#Inital Conditions
lowX = 2.5
highX = 4

#initalize variables
lowXCurrent = 0
highXCurrent = 0
meanX = 0
meanXList = []
timeList = []
for i in range(15): #Iterating for 15 times
    meanCurrent = None
    meanX = (lowX + highX)/2
    meanXList.append(meanX)
    for index, line in enumerate(timeList): #Checks every time value in TimeList and assigns the time values to corresponding current values
        if line == lowX:
            lowXCurrent = currentList[index]
        if line == highX:
            highXCurrent = currentList[index]
        if line == meanX:
            meanCurrent = currentList[index]
    if meanCurrent == None:
        print(f'Mean time value of {meanX} not found in data set')
        break
    if lowXCurrent < 0 and meanCurrent < 0 or lowXCurrent > 0 and meanCurrent > 0:
        lowX = meanX
    elif highXCurrent < 0 and meanCurrent < 0 or highXCurrent > 0 and meanCurrent > 0:
        highX = meanX
    print(meanX)
