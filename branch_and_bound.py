import numpy as np
import fractions
from ortools.algorithms import pywrapknapsack_solver
import math

def convert_fractions_to_integers(fraction):
  lcm = fractions.Fraction(fraction[0]).limit_denominator().denominator
  for fractio in fraction:
    lcm = math.lcm(lcm, fractions.Fraction(fractio).limit_denominator().denominator)

  integers = []
  for fractio in fraction:
    integers.append(fractions.Fraction(fractio).limit_denominator().numerator * lcm // fractions.Fraction(fractio).limit_denominator().denominator)

  return integers

def branch_and_bounds(new_width,new_Y,total_width,width,Y):
    weights_ = np.array([])
    new_Y_ = np.array(convert_fractions_to_integers(new_Y.tolist()))
    values_ = np.array([])
    pattern = np.zeros_like(new_width)
    for i in range(len(new_width)):
        for j in range(int(total_width/new_width[i])):
            weights_ = np.append(weights_, new_width[i])
            values_ = np.append(values_,new_Y_[i])
    values = values_.tolist()
    weights = np.reshape(weights_,[1,weights_.shape[0]]).tolist()
    capacity = [total_width]
    P = np.array(knapsack_solver(values,weights,capacity))
    for i in P:
        index = np.where(width == i)
        pattern[index] += 1
    #print(pattern)
    if np.sum(pattern*Y) <= 1:
       return 0
    return pattern


def knapsack_solver(values, weights, capacities):
    solver = pywrapknapsack_solver.KnapsackSolver(
    pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()
    packed_items = []
    packed_weights = []
    total_weight = 0
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    return packed_weights;