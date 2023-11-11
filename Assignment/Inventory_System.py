import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time

totalday = random.randint(80,100)

inventory = random.randint(1,10)
print(f'Current inventory level : {inventory}')
timeNeedArrive = random.randint(8,15)
print(f'Time needed for a product to arrive: {timeNeedArrive}')
order_range  = [3, 12]
low = order_range [0]
high = order_range [1]
days = [8, 17, 26, 47, 53, 62, 65, 68, 77]
np.random.seed(42)
value = np.random.choice(np.arange(1, 8), size=9, p=[1/7]*7)

print(f'Days on which orders are placed: {days}')
print(f'Demand values for each day: {value}')

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


for _ in range(totalday + 1):
    my_function()


holdingCost = 0.0
backlogCost = 0.0
j = 1

for i in range(0, totalday):
    if (inventoryDetails[i] > 0):
        holdingCost += inventoryDetails[i]
    if (inventoryDetails[i] < 0):
        backlogCost += abs(inventoryDetails[i])
    print("Day :", j, "Inventory level: ", inventoryDetails[i])
    j += 1

print(f'Total accumulated cost of holding:{holdingCost}')
print(f'Total accumulated cost of backlogged orders:{backlogCost}') 

perHoldingCost = 12.0
perBacklogCost = 30.0

print("Avarage holding cost: ", holdingCost * perHoldingCost / totalday)
print("Avarage backlog cost: ", backlogCost * perBacklogCost / totalday)

temp = np.arange(len(inventoryDetails))
zeross = np.zeros(len(inventoryDetails))

def animate(i):
    plt.clf()
    plt.plot(temp[:i], inventoryDetails[:i], drawstyle='steps', color="red")
    plt.plot(temp[:i], zeross[:i], drawstyle='steps')
    plt.title('Step Line Plot')
    plt.xlabel("Time")
    plt.ylabel("Inventory level")
    plt.grid()

fig = plt.figure()
ani = FuncAnimation(fig, animate, frames=len(temp), interval=100, repeat=False)

plt.show()







