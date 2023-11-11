import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Total number of days in the simulation
total_days = 105

# Initial inventory and parameters
initial_inventory = 4
time_needed_to_arrive = 13
order_range = [3, 5]
low_order_limit = order_range[0]
high_order_limit = order_range[1]

# Days when demand occurs and corresponding values
demand_days = [18, 27, 36, 57, 63, 72, 75, 78, 87]
demand_values = [4, 3, 2, 3, 1, 2, 3, 3, 4]

# Arrays to store data
order_arrival = np.zeros(total_days + time_needed_to_arrive + 1)
inventory_details = []
daily_value = np.zeros(total_days + 1)  # Modify array size here

current_day = 1
# Process demand days and values
while current_day <= total_days:
    while len(demand_values) > 0 and current_day == demand_days[0]:
        daily_value[current_day] += demand_values[0]
        demand_values = np.delete(demand_values, 0)
        demand_days = np.delete(demand_days, 0)
    current_day += 1

def process_day():
    global current_day, demand_values, initial_inventory

    if current_day % 30 == 0 and low_order_limit > initial_inventory:
        order_arrival[current_day + time_needed_to_arrive] = high_order_limit - initial_inventory

    if order_arrival[current_day] > 0:
        initial_inventory += order_arrival[current_day]
        order_arrival[current_day] = 0

    if daily_value[current_day] > 0:
        initial_inventory -= daily_value[current_day]
    inventory_details.append(initial_inventory)
    current_day += 1

# Process each day
for _ in range(total_days + 1):
    process_day()

# Calculate holding and backlog costs
holding_cost = 0.0
backlog_cost = 0.0
day_count = 1

for inventory_level in inventory_details:
    if inventory_level > 0:
        holding_cost += inventory_level
    if inventory_level < 0:
        backlog_cost += abs(inventory_level)
    print("Day:", day_count, "Inventory level:", inventory_level)
    day_count += 1

print("Holding cost:", holding_cost)
print("Backlog cost:", backlog_cost)

# Per month costs
per_holding_cost = 12.0
per_backlog_cost = 30.0

print("Average holding cost:", holding_cost * per_holding_cost / total_days)
print("Average backlog cost:", backlog_cost * per_backlog_cost / total_days)

# Create animation
temp = np.arange(len(inventory_details))
zero_array = np.zeros(len(inventory_details))

def animate(i):
    plt.clf()
    plt.plot(temp[:i], inventory_details[:i], drawstyle='steps', color="red")
    plt.plot(temp[:i], zero_array[:i], drawstyle='steps')
    plt.title('Step Line Plot')
    plt.grid()

fig = plt.figure()
ani = FuncAnimation(fig, animate, frames=len(temp), interval=100, repeat=False)

plt.show()
