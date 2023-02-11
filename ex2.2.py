# ENSF 338 Assignment 2
# Sufyan Ayaz (30142184) amd Taha Khan (30145085)

import json
import timeit
import matplotlib.pyplot as plt
import sys
import threading
threading.stack_size(33554432)

sys.setrecursionlimit(20000)


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)


def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


with open("ex2JSON.json", "r") as exercise_data:
    data_list = json.load(exercise_data)

timings = []

for i in range(len(data_list)):
    data = data_list[i][:]

    time = timeit.repeat('func1(data_copy, 0, len(data_copy)-1)',
                         setup='data_copy = data[:]',
                         globals={'data': data, 'func1': func1},
                         repeat=1,
                         number=1)

    timings.append(time)

plt.plot(timings, color="c")
plt.title("Quicksort Algorithm Timing Results")
plt.ylabel("Time")
plt.xlabel("Dataset")
plt.show()
