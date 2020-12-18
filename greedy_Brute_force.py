###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import random

#================================
# Part A: Transporting Space Cows
#================================

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
    
    File_object = open(filename,'r')
    cowdata={}
    cows=[]
    number_of_objects=0
    for n_line in File_object:
 # store the cows in a list and remove the spaces and the newlines  
      cows.append(n_line.strip())
      cow_n_data=cows[number_of_objects].split(',')
      number_of_objects +=1
      cowdata[cow_n_data[0]]=cow_n_data[1]
    return cowdata
# creating a function to sum lists even empty lists
def sum_list(list):
    """
    

    Parameters
    ----------
    list : it take a list even an empty one .

    Returns
    -------
    result : return 0 if the list is empty and the sum otherwise

    """
    if list==[]:
        result=0
    else:
     result=0
     for i in list :
        result += i
    return (result)    

# Problem 2
def greedy_cow_transport(cows,limit):
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
    start=time.time()
    cows_copy=cows.copy()
    # the list that contains all trips every trip has a list containing the cows to be transported
    cows_final_trip_lists=[]
    #while len(cows_copy)

    while bool(cows_copy)== True:
       #creating a list of names and values for the cows to be transported in this trip
       for key in cows_copy:
           cows_copy[key]=int(cows_copy[key])
           
       cows_transporting_list_names=[]
       cows_transporting_list_values=[]
       #this while loop is to create a single trip  
       while bool(cows_copy) == True:
           # getting the current maximum name and value
           current_max_name=max(cows_copy,key=cows_copy.get)
           current_max_value=max(cows_copy.values())
           #adding this current maximum to a list to check if they exceed the criteria of 10 ton 
           cows_transporting_list_names.append(current_max_name)
           cows_transporting_list_values.append(int(current_max_value))
           # removing the current maximum value from the copied dictionary 
           del cows_copy[current_max_name]
           # checking if the list meet the criteria of 10 ton or not 
           if sum_list(cows_transporting_list_values) > limit:
               # this piece of code will only be excuted if the current maximum is higher than the criteria of 10 ton 
               cows_transporting_list_names.pop(-1)
               cows_transporting_list_values.pop(-1)
       # updating the trip lists . its a list of lists. every list describe a trip
       cows_final_trip_lists.append(cows_transporting_list_names)    
       # creating a new list of the cows after removing the ones that already transported
       cows_copy=cows.copy()
       for i in cows_final_trip_lists:
          for n in i:
             del cows_copy[n]
    end=time.time()
    time_taken=end-start
    return(cows_final_trip_lists,time_taken)
# Problem 3
def brute_force_cow_transport(cows,limit=10):
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
    start=time.time()
    for key in cows:
      cows[key]=int(cows[key])
    
    sum_cows = 0
    cows_final_trip_lists=[]
    cows_final_trip_list=[]

     #the point here is to minimize the number of trips that will be taken 
    for partition in get_partitions(cows):
       number_of_partitions=len(partition)
       iteration = 0 
       #print(partition)
       for n in partition:
            #print(n)
            for i in n:
                sum_cows += cows[i]
            #print(sum_cows)
            if sum_cows > 10 and not (cows_final_trip_lists):
                break
            elif sum_cows >10 and (cows_final_trip_lists):
                cows_final_trip_lists=[]
                break
            elif sum_cows <= 10:
                cows_final_trip_lists.append(n)
                iteration +=1
                sum_cows = 0
       sum_cows = 0
       if iteration == number_of_partitions:
          #print(cows_final_trip_lists)
          cows_final_trip_list.append(cows_final_trip_lists)
          cows_final_trip_lists=[]
    number_of_trips=[]
    for i in cows_final_trip_list:
      number_of_trips.append(len(i)) 
    minimum_number_of_trips=min(number_of_trips)
    indices = [index for index, element in enumerate(number_of_trips) if element == minimum_number_of_trips]
    list_of_cows_with_min_numberoftrips=[]
    for i in range(len(indices)):
      list_of_cows_with_min_numberoftrips.append(cows_final_trip_list[indices[i]])
    Brute_force_cow_transport=random.choice(list_of_cows_with_min_numberoftrips)
    end=time.time()
    time_taken=end-start
    return(Brute_force_cow_transport,time_taken)
        
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
    cow_list=('ps1_cow_data.txt')
    cows=(load_cows(cow_list))
    limit=10
    greedy_algorithm_result=greedy_cow_transport(cows,limit)
    brute_force_results=brute_force_cow_transport(cows,limit)
    greedy_algorithm_trips=greedy_algorithm_result[0]
    greedy_algorithm_number_of_trips=len(greedy_algorithm_result[0])
    greedy_algorithm_time_taken=greedy_algorithm_result[1]
    brute_force_algorithm_trips=brute_force_results[0]
    brute_force_algorithm_number_of_trips=len(brute_force_results[0])
    brute_force_algorithm_time_taken=brute_force_results[1]
   
    
    print('the answer of the greedy algorithm is :')
    print(greedy_algorithm_trips)
    print ('number of trips for greedy algorithm is  '+str(greedy_algorithm_number_of_trips)+' time taken is '+str(greedy_algorithm_time_taken))
    print('the answer of the Brute force algorithm is :')
    print(brute_force_algorithm_trips)
    print ('number of trips for brute force algorithm is  '+str(brute_force_algorithm_number_of_trips)+' time taken is '+str(brute_force_algorithm_time_taken))
compare_cow_transport_algorithms()