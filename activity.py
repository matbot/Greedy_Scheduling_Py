#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 2/3/2019
    Activity Selection Last-to-Start
    Description: A Python implementation of a greedy algorithm to schedule maximal activities.
    Reads lists of activities from a file, act.txt, then uses a merge sort + greedy algorithm to select an optimal set of
    activities to allow the greatest number of activities to be scheduled based on the latest start times.
    The optimal sets are printed to the terminal organized by activity number.
"""

## Merge function to service descending mergesort.
def merge(array, start, midpoint, end):
    n1 = midpoint + 1
    left_array = array[start:n1]  # separate the subarrays to be merged.
    right_array = array[n1:end + 1]
    left_array.append({'activity_number': float("inf"), 'start_time': float("-inf"), 'finish_time': float("-inf")})  # -inf used for descending sort.
    right_array.append({'activity_number': float("inf"), 'start_time': float("-inf"), 'finish_time': float("-inf")})
    i = j = 0
    for k in range(start, end + 1):  # merge the partial arrays to a combined, ordered array.
        if left_array[i]['start_time'] > right_array[j]['start_time']:    # merge the arrays based on descending start time!!
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1

## Descending recursive mergesort.
def mergesort(array, start, end):
    if start < end:
        midpoint = (start + end) // 2  # floor division --Python3
        mergesort(array, start, midpoint)
        mergesort(array, midpoint + 1, end)
        merge(array, start, midpoint, end)

## Greedy selection based on latest start.
def last_start(activity_list):
    mergesort(activity_list, 0, len(activity_list) - 1)
    selected_activities = [activity_list[0]]
    current_start = activity_list[0]['start_time']
    for x in range(1, len(activity_list)):
        if activity_list[x]['finish_time'] <= current_start:
            selected_activities.append(activity_list[x])
            current_start = activity_list[x]['start_time']
    return selected_activities


# MAIN
if __name__ == "__main__":
    with open("act.txt", "r") as f:  # read and parse activity list from file.
        activity_count = f.readline()
        set_number = 1
        while activity_count:
            activity_count = int(activity_count)
            activities = []
            for activity in range(activity_count):
                line = f.readline()
                line = line.split()
                activities.append({'activity_number': int(line[0]), 'start_time': int(line[1]), 'finish_time': int(line[2])})
            activities = list(reversed(last_start(activities)))
            activity_numbers = []
            for i in activities:
                activity_numbers.append(i['activity_number'])

            print("Set {}".format(set_number))
            print("Number of activities selected = {}".format(len(activities)))
            print("Activities: {} \n".format(str(activity_numbers)[1:-1]))

            activity_count = f.readline()
            set_number += 1
