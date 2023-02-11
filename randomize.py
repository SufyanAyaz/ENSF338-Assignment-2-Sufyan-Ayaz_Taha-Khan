# ENSF 338 Assignment 2
# Sufyan Ayaz (30142184) amd Taha Khan (30145085)

import json
import random

with open("ex2JSON.json", "r") as exercise_data:
    data_list = json.load(exercise_data)

randomized = []

for i in range(len(data_list)):
    data = data_list[i][:]
    random.shuffle(data)
    randomized.append(data)


with open("ex2.5.json", "w") as rand:
    json.dump(randomized, rand)
