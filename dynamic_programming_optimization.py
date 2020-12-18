###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
from ps1_partition import get_partitions
def sum_list(list):
    if list==[]:
        result=0
    else:
     result=0
     for i in list :
        result += i
    return (result)
# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # dynamic prograaming is about making the bigger problem into small proplems and store it then 
    #the stored values multiple time
    # in this part I am getting all possible combination of the eggs weight so if we have 5 different weights 
    # that mean we will have like 31 different combination of unique values 
    for partition in get_partitions(egg_weights):
      for i in partition :
        the_sum_list=sum_list(i)
        memo[the_sum_list]=i
    all_possible_combination_list=[]
    all_possibble_combination_values=[]
    possible_solutions=[]
    possible_eggs=[]

    for i in memo.values():
      all_possible_combination_list.append(i)
    for i in memo.keys():
      all_possibble_combination_values.append(i)
    # here I made it a new proplem while the only thing the code is trying to do is to try to maximize
    # the weight while not excedding the target weight value 
    while all_possibble_combination_values:
      weight_of_the_eggs=0
      list_of_the_eggs=[]
      number_of_nodes=len(all_possibble_combination_values)
      for i in range(number_of_nodes-1):
        if all_possibble_combination_values[i] > all_possibble_combination_values[i+1]:
            weight_of_the_eggs += all_possibble_combination_values[i]
            list_of_the_eggs.append(all_possible_combination_list[i])
            if weight_of_the_eggs> target_weight:
              weight_of_the_eggs -= all_possibble_combination_values[i]
              list_of_the_eggs.pop()
      all_possibble_combination_values.pop(0)
      all_possible_combination_list.pop(0)
      possible_solutions.append(weight_of_the_eggs)
      possible_eggs.append(list_of_the_eggs)
    the_optimal_solution=max(possible_solutions)
    the_optimal_solution_index=possible_solutions.index(the_optimal_solution)
    the_optimal_solution_list=possible_eggs[the_optimal_solution_index]
    # this part is checking if I have any repetitive values inside my optimal solution in which I can 
    # add together to perform just one egg so if I have two eggs of 10 that makes it one of 20 and so on 
    
    the_optimal_solution_list2=[] 
    for i in the_optimal_solution_list:
     for n in i :
        the_optimal_solution_list2.append(n)

    for idx, val in enumerate(the_optimal_solution_list2):
     iteration=0
     for idx2,val2 in enumerate(the_optimal_solution_list2):
        Z=val+val2 
        if Z in egg_weights and idx != idx2 and iteration==0:
            
            the_optimal_solution_list2.remove(val)
            the_optimal_solution_list2.remove(val2)
            the_optimal_solution_list2.append(Z)
            iteration += 1
    # this part is checking if I still have space in my knapsack or my ship to add the smallest ever 
    # egg       
    k=target_weight-sum_list(the_optimal_solution_list2)

    while  k >=min(egg_weights):
     the_optimal_solution_list2.append(min(egg_weights))
     k=target_weight-sum_list(the_optimal_solution_list2)    
    return(the_optimal_solution_list2)  

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 2, 5,10, 20)
    n = 99
    print("Egg weights = (1,2, 5, 10, 20)")
    print("n = 99")
    print("Expected ouput: 8 (4 * 20 + 1 * 10 + 1 * 5 +2 * 2= 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    egg_weights = (1, 2, 5, 17,18, 20)
    n = 99
    print("Egg weights = (1,2, 5, 10, 20)")
    print("n = 99")
    print("Expected ouput: 6 (4 * 20 + 1 * 17 + 1 * 2 )" " or ( 4 * 20 + 1 * 18 + 1 * 1)" "or ( 2 * 20 + 3 * 18 + 1 * 5 )")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()