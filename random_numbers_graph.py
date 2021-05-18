import random
import numpy as np
import matplotlib.pyplot as plt

from utils import *

# this program creates a list of random numbers and counts each item in list
# then creates a distinct list of the contents in the original list
# and lines them up with another list of their number of occurrences.
# Then, creates a graph of the data collected via output manipulation.
# example:
# [4, 1, 3, 2, 1, 1, 2, 2, 0, 3]
# Distinct list: [4, 1, 3, 2, 0]
#   occurrences: [1, 3, 2, 3, 1]
# 4 occurs 1 time, 1 occurs 3 times.

# this program can be used to collect data in a list, count them, and display their occurrences.

num_list = []
# for i in range(quantity of numbers generated)
number_of_values = 21

# (i * i + 2 * i + 1) // (number_of_values * 50)
from math import factorial


def algorithm(i):
    some = factorial(i)
    value = some % number_of_values
    return value


for i in range(number_of_values):  # choose here a format with which to generate the numbers in your list.
    num_list.append(random.randint(0, algorithm(i)))  # linear, quadratic, etc.

print(num_list)  # original list

# initializing most frequent number in list for find max functionality
most_common_num_count = num_list.count(num_list[0])
integer_stored = num_list[0]

for integer in num_list:
    if most_common_num_count < num_list.count(integer):
        integer_stored = integer
        most_common_num_count = num_list.count(integer)

distinct_list = create_distinct_list(num_list)
distinct_list_counts = []

for item in distinct_list:
    distinct_list_counts.append(num_list.count(item))

numbers_dictionary = dict(zip(distinct_list, distinct_list_counts))

dict_values = sorted(numbers_dictionary.values())
dict_values.reverse()

dict_keys = numbers_dictionary.keys()

numbers_dictionary = dict(zip(dict_keys, dict_values))

print(numbers_dictionary.values())

print(f"numbers: {list(numbers_dictionary.keys())}")

print(f"\nThe integer that repeated the most was {integer_stored}, at {most_common_num_count} times.")

for x in dict_keys:
    spaces = ' ' * (4 - len(str(x)))
    print(f"{spaces}{x}: {'|' * numbers_dictionary[x]}")
