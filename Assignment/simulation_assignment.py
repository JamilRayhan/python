import numpy as np
import matplotlib.pyplot as plt

## Inventory system
totalday = 90

# n=int(input("Enter number of Day : "))
# inventory=int(input("Initial inventory level : "))
# timeNeedArrive=int(input("Product arrival time after order: "))
# temp=list(map(int,input("Inventory min,max level : ").split()))
# days=np.random.randint(1,totalday,n)
# days=np.sort(days)
# value=np.random.randint(1,5,n)
# print(days)
# print(value)

n = int(9)
inventory = int(4)
timeNeedArrive = int(13)
temp = [3, 5]
low = temp[0]
high = temp[1]
days = [18, 27, 36, 57, 63, 72, 75, 78, 87]
value = [4, 3, 2, 3, 1, 2, 3, 3, 4]

print(days)
print(value)

dy = 0
orderArrive = np.zeros(totalday + timeNeedArrive + 1)
inventoryDetails = []
dayValue = np.zeros(totalday + 5)

i = 1
while i <= totalday:
    while len(value) > 0 and i == days[0]:
        dayValue[i] += value[0];
        value = np.delete(value, 0)
        days = np.delete(days, 0)
    i += 1


def my_function():
    global dy, value, inventory

    if dy % 30 == 0 and low > inventory:
        orderArrive[dy + timeNeedArrive] = high - inventory

    if orderArrive[dy] > 0:
        inventory += orderArrive[dy]
        orderArrive[dy] = 0

    if dayValue[dy] > 0:
        inventory -= dayValue[dy]
    inventoryDetails.append(inventory)
    dy += 1


###### Start from here ######
##### Main funciton #########
for _ in range(totalday + 1):
    my_function()

# print(inventoryDetails)
holdingCost = 0.0
backlogCost = 0.0
j = 1

for i in range(0, totalday):
    if (inventoryDetails[i] > 0):
        holdingCost += inventoryDetails[i]
    if (inventoryDetails[i] < 0):
        backlogCost += abs(inventoryDetails[i])
    print("Day : ", j, "Inventory level: ", inventoryDetails[i])
    j += 1

print(holdingCost, backlogCost)
# perHoldingCost=int(input("Enter per holding cost :"))
# perBacklogCost=int(input("Enter per backlog cost :"))
perHoldingCost = 12.0
perBacklogCost = 30.0
# j=1;
# for i in inventoryDetails:
#     print(j,i)
#     j+=1


print("Avarage holding cost: ", holdingCost * perHoldingCost / totalday)
print("Avarage backlog cost: ", backlogCost * perBacklogCost / totalday)

temp = np.arange(len(inventoryDetails))
zeross = np.zeros(len(inventoryDetails))
plt.figure()
plt.plot(temp, inventoryDetails, drawstyle='steps', color="blue")
plt.plot(temp, zeross, drawstyle='steps')
plt.title('Step Line Plot')
plt.grid()
plt.show()
