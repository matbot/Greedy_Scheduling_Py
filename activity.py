#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Author: Mathew McDade
    Date: 2/3/2019
    Class: CS325.400 Winter 2019
    Assignment: HW4: Activity Selection Last-to-Start
    Description: A Python implementation of a greedy algorithm to schedule maximal activities.
    Read lists of activities from a file, act.txt, then uses a greedy algorithm to select an optimal set of
    activities to allow the greatest number of activities to be scheduled based on the latest start times.
    The optimal sets are printed to the terminal organized by activity number.
"""


def merge(array, start, midpoint, end):
    n1 = midpoint + 1
    left_array = array[start:n1]  # separate the subarrays to be merged.
    right_array = array[n1:end + 1]
    left_array.append({'n': float("inf"), 's': float("-inf"), 'f': float("-inf")})  # -inf used for descending sort.
    right_array.append({'n': float("inf"), 's': float("-inf"), 'f': float("-inf")})
    i = j = 0
    for k in range(start, end + 1):  # merge the partial arrays to a combined, ordered array.
        if left_array[i]['s'] > right_array[j]['s']:    # merge the arrays based on descending start time!!
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def mergesort(array, start, end):
    if start < end:
        midpoint = (start + end) // 2  # floor division --Python3
        mergesort(array, start, midpoint)
        mergesort(array, midpoint + 1, end)
        merge(array, start, midpoint, end)


def last_start(activity_list):
    mergesort(activity_list, 0, len(activity_list) - 1)     # mergesort adapted from previous assignment.
    selected_activities = [activity_list[0]]
    current_start = activity_list[0]['s']
    for x in range(1, len(activity_list)):
        if activity_list[x]['f'] <= current_start:
            selected_activities.append(activity_list[x])
            current_start = activity_list[x]['s']
    return selected_activities


# MAIN
if __name__ == "__main__":
    with open("act.txt", "r") as f:  # read and parse integer lists from file.
        activity_count = f.readline()
        set_number = 1
        while activity_count:
            activity_count = int(activity_count)
            activities = []
            for activity in range(activity_count):
                line = f.readline()
                line = line.split()
                activities.append({'n': int(line[0]), 's': int(line[1]), 'f': int(line[2])})
            activities = list(reversed(last_start(activities)))
            activity_numbers = []
            for i in activities:
                activity_numbers.append(i['n'])

            print("Set {}".format(set_number))
            print("Number of activities selected = {}".format(len(activities)))
            print("Activities: {} \n".format(str(activity_numbers)[1:-1]))

            activity_count = f.readline()
            set_number += 1
