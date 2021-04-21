import numpy as np

states = ["Work","Bed","Gym"]
kombinacije = [["WW","WB","WG"], ["BW","BB","BG"],["GW","GB","GG"]]
transitionMatrix = [[0.5,0.4,0.1],[0.3,0.2,0.5],[0.7,0.1,0.2]]

def result(days):
    activityToday = "Work"
    print("Start state: " + activityToday)
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Work":
            change = np.random.choice(kombinacije[0],replace=True,p=transitionMatrix[0])
            if change == "WW":
                prob = prob * 0.5
                activityList.append("Work")
                pass
            elif change == "WB":
                prob = prob * 0.4
                activityToday = "Bed"
                activityList.append("Bed")
            else:
                prob = prob * 0.1
                activityToday = "Gym"
                activityList.append("Gym")
        elif activityToday == "Bed":
            change = np.random.choice(kombinacije[1],replace=True,p=transitionMatrix[1])
            if change == "BB":
                prob = prob * 0.2
                activityList.append("Bed")
                pass
            elif change == "BW":
                prob = prob * 0.3
                activityToday = "Work"
                activityList.append("Work")
            else:
                prob = prob * 0.5
                activityToday = "Gym"
                activityList.append("Gym")
        elif activityToday == "Gym":
            change = np.random.choice(kombinacije[2],replace=True,p=transitionMatrix[2])
            if change == "GG":
                prob = prob * 0.2
                activityList.append("Gym")
                pass
            elif change == "GW":
                prob = prob * 0.7
                activityToday = "Work"
                activityList.append("Work")
            else:
                prob = prob * 0.1
                activityToday = "Bed"
                activityList.append("Bed")
        i += 1
    print("States: " + str(activityList))
    print("After "+ str(days) + " days the state will be: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

result(3)

def result(days):
    activityToday = "Work"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Work":
            change = np.random.choice(kombinacije[0],replace=True,p=transitionMatrix[0])
            if change == "WW":
                prob = prob * 0.5
                activityList.append("Work")
                pass
            elif change == "WB":
                prob = prob * 0.4
                activityToday = "Bed"
                activityList.append("Bed")
            else:
                prob = prob * 0.1
                activityToday = "Gym"
                activityList.append("Gym")
        elif activityToday == "Bed":
            change = np.random.choice(kombinacije[1],replace=True,p=transitionMatrix[1])
            if change == "BB":
                prob = prob * 0.2
                activityList.append("Bed")
                pass
            elif change == "BW":
                prob = prob * 0.3
                activityToday = "Work"
                activityList.append("Work")
            else:
                prob = prob * 0.5
                activityToday = "Gym"
                activityList.append("Gym")
        elif activityToday == "Gym":
            change = np.random.choice(kombinacije[2],replace=True,p=transitionMatrix[2])
            if change == "GG":
                prob = prob * 0.2
                activityList.append("Gym")
                pass
            elif change == "GW":
                prob = prob * 0.7
                activityToday = "Work"
                activityList.append("Work")
            else:
                prob = prob * 0.1
                activityToday = "Bed"
                activityList.append("Bed")
        i += 1
    return activityList

list_activity = []
count = 0

for iterations in range(1,10000):
        list_activity.append(result(3))


for smaller_list in list_activity:
    if(smaller_list[2] == "Bed"):
        count += 1
percentage = (count/10000) * 100
print("The probability of starting at state:'Work' and ending at state:'Bed'= " + str(percentage) + "%")

