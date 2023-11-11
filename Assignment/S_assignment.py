import threading
import time
import random
import matplotlib.pyplot as plt

# Constants
NUM_EVENTS = 10
MAX_SERVICE_TIME = 100

# Shared variables
event_list = []
clock = 0
total_service_time = 0
total_waiting_time = 0
total_queue_length = 0
total_idle_time = 0
lock = threading.Lock()

def generate_event():
    return (random.randint(1, 100), random.randint(1, MAX_SERVICE_TIME))

def event_handler(thread_num, event, plot_data):
    global clock, total_service_time, total_waiting_time, total_queue_length, total_idle_time

    arrival_time, service_time = event
    with lock:
        if clock < arrival_time:
            total_idle_time += arrival_time - clock
            clock = arrival_time
        else:
            total_waiting_time += clock - arrival_time
            total_queue_length += clock - arrival_time  # Increment queue length by waiting time
        total_queue_length += 1

    print(f"Thread {thread_num}: Event started at time {clock}: {event}")
    time.sleep(service_time / 1000)  # Simulating service time in seconds

    with lock:
        clock += service_time
        total_service_time += service_time
        total_queue_length -= 1 if total_queue_length > 0 else 0

    print(f"Thread {thread_num}: Event finished at time {clock}")

    # Plotting
    with lock:
        plot_data.append((thread_num, arrival_time, service_time, clock - arrival_time))

def main():
    global event_list
    event_list = [generate_event() for _ in range(NUM_EVENTS)]
    plot_data = []

    threads = []
    for i, event in enumerate(event_list):
        thread = threading.Thread(target=event_handler, args=(i+1, event, plot_data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    avg_service_time = total_service_time / NUM_EVENTS
    avg_waiting_time = total_waiting_time / NUM_EVENTS
    avg_queue_length = sum([item[3] for item in plot_data]) / len(plot_data)  # Sum of waiting times
    avg_idle_time = total_idle_time / NUM_EVENTS

    print("\nSimulation Results:")
    print(f"Average Service Time: {avg_service_time:.2f} units")
    print(f"Average Waiting Time: {avg_waiting_time:.2f} units")
    print(f"Average Queue Length: {avg_queue_length:.2f} members")
    print(f"Average Idle Time: {avg_idle_time:.2f} units")

    # Configure the plot
    plt.xlabel('Time')
    plt.ylabel('Thread')
    plt.title('Thread Operations')

    for thread_num, arrival_time, service_time, waiting_time in plot_data:
        plt.barh(thread_num, service_time, left=arrival_time, color='blue', label='Service Time')
        plt.barh(thread_num, waiting_time, left=arrival_time + service_time, color='gray', label='Waiting Time')

    plt.legend()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
