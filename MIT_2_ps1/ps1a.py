###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#   ================================
# Part A: Transporting Space Cows
#   ================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_dict = {}
    with open(filename) as opened_file:
        for line in opened_file:
            current_line = line.split(',')
            cow_dict[current_line[0]] = int(current_line[1])

    return cow_dict


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    current_trip = []
    trip_list = []
    trip_weight = 0
    cows_sorted = sorted(list(cows.items()), key=lambda x: x[1], reverse=True)
    while len(cows_sorted):
        cows_copy = cows_sorted[:]
        for cow in cows_copy:
            if trip_weight + cow[1] <= limit:
                current_trip.append(cow[0])
                trip_weight += cow[1]
                cows_sorted.remove(cow)
        trip_list.append(current_trip)
        trip_weight = 0
        current_trip = []

    return trip_list


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cows_list = list(cows.items())
    trip_list = cows_list
    trip_max = True

    for trip_combo in get_partitions(cows_list):
        trip_set = []
        for trip in trip_combo:
            current_trip = []
            trip_max = True
            trip_cost = 0
            for cow in trip:
                trip_cost += cow[1]
                current_trip.append(cow[0])
            trip_set.append(current_trip)
            if trip_cost > limit:
                trip_max = False
                break
        if trip_max & (len(trip_set) < len(trip_list)):
            trip_list = trip_set

    return trip_list


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cow_dict = load_cows('ps1_cow_data.txt')
    time_start = time.perf_counter()
    greedy_trip = greedy_cow_transport(cow_dict, 10)
    time_end = time.perf_counter()
    greedy_time = time_end - time_start

    time_start = time.perf_counter()
    brutal_trip = brute_force_cow_transport(cow_dict, 10)
    time_end = time.perf_counter()
    brutal_time = time_end - time_start

    print(f"The greedy method took {greedy_time} seconds to run and found {len(greedy_trip)} trips")
    print(f"The brute force method took {brutal_time} seconds to run and found {len(brutal_trip)} trips")


compare_cow_transport_algorithms()
