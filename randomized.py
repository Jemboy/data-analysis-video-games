import matplotlib.pyplot as plotOp
import numpy as np
from random import randint
import re as regexOp

filename = "devolver.txt"
regexCode = r"<game name=\"(.*)\" price=\"(.*)\" owners=\"(.*)\""

with open(filename, "r") as dataFile:
    dataLines = [line for line in dataFile]

nameData, priceData, ownerData = [], [], []
for line in dataLines:
    tokens = regexOp.search(regexCode, line)
    if tokens:
        name, price, owners = tokens.groups()
        price, owners = float(price), float(owners)
        nameData.append(name)
        priceData.append(price)
        ownerData.append(owners)
        print("Name is \"%s\", price is %d and number of owners is %d." % (name, price, owners))
figVal, axVal = plotOp.subplots()

# Create random priceData here
randomData = []
for index in range(1000):
    randomNumber = float(randint(0, 59))
    randomNumber += 0.99
    randomData.append(randomNumber)

axVal.hist(randomData, bins = np.arange(0.99, max(randomData) + 2) - 0.5)

xTicks = []
singleTick = 0.99

while singleTick <= max(randomData):
    xTicks.append(singleTick)
    singleTick += 1
axVal.set_xticks(xTicks)

tempVal, xLabels = plotOp.xticks()
plotOp.setp(xLabels, rotation = 90)

axVal.set_title("Correlation Between Sales and Prices")
axVal.set_xlabel("Prices")
axVal.set_ylabel("Frequency")
axVal.grid(True)
plotOp.show()