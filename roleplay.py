import matplotlib.pyplot as plotOp
import numpy as np

filename = "roleplay.txt"
with open(filename, "r") as dataFile:
    dataLines = [line for line in dataFile]

scoreAndHours = {}
scoreInterval, index = 4, 0
while scoreInterval * index < 100:
    scoreAndHours.update({scoreInterval * index: []})
    index += 1

scoreKeys = list(scoreAndHours.keys())
for dataLine in dataLines:
    dataLine = dataLine.split()
    score = dataLine[-6]
    if score == "N/A":
        pass
    else:
        score = float(score.replace('%', ''))
        hours = float(dataLine[-2].split(':')[0])

        currentKey = 0
        for index in range(len(scoreKeys) - 1):
            if score >= scoreKeys[index] and score < scoreKeys[index + 1]:
                currentKey = scoreKeys[index]
                scoreAndHours[currentKey].append(hours)
                break
        else:
            currentKey = scoreKeys[len(scoreKeys) - 1]
            scoreAndHours[currentKey].append(hours)

averageHours = []
for mKey in scoreAndHours:
    hoursList = scoreAndHours[mKey]
    averageHours.append(float(sum(hoursList)) / len(hoursList))

figVal, axVal = plotOp.subplots()
x, y = np.array(scoreKeys), np.array(averageHours)
polyFit = np.polyfit(x, y, deg = 1)
axVal.plot(x, polyFit[0] * x + polyFit[1], color = 'red')
axVal.scatter(x, y)

axVal.set_xticks(scoreKeys)
tempVal, xLabels = plotOp.xticks()

axVal.set_title("Correlation of Score Percentage and Hours Played for the Roleplay Genre")
axVal.set_xlabel("Score Percentage")
axVal.set_ylabel("Hours Played")
axVal.grid(True)
plotOp.show()