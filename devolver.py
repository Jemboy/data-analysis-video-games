import matplotlib.pyplot as plotOp
import numpy as np

filename = "devolver.txt"
with open(filename, "r") as dataFile:
    dataLines = [line for line in dataFile]

nameData, priceData, ownerData = [], [], []
for dataLine in dataLines:
    dataLine = dataLine.split()
    name = dataLine[1: len(dataLine) - 10]
    if dataLine[-7] == "Free":
        price = 0
    else:
        price = float(dataLine[-7][1:])
    owners = dataLine[-4]

    nameData.append(name)
    priceData.append(price)
    ownerData.append(owners)

figVal, axVal = plotOp.subplots()
axVal.hist(priceData, bins = np.arange(0.99, max(priceData) + 2) - 0.5)

xTicks = []
singleTick = 0.99
while singleTick <= max(priceData):
    xTicks.append(singleTick)
    singleTick += 1
axVal.set_xticks(xTicks)

tempVal, xLabels = plotOp.xticks()
plotOp.setp(xLabels, rotation = 90)

axVal.set_title("Frequency of Price Tags")
axVal.set_xlabel("Prices in Dollars")
axVal.set_ylabel("Frequency")
axVal.grid(True)
plotOp.show()