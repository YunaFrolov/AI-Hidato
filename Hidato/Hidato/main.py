#coding : utf-8
__author__ = 'Yuna Phrolov'


import Game as G
import Heuristics as H
import time


dictOfStates = {}


# updates the heuristics for each state in the set of states given
def updateState(setOfStates):
    for s in setOfStates:
        dictOfStates[s] = heuristic.H(s)
    return dictOfStates


# chooses the maximum heuristic state of all available
def argMax(setOfStates):
    v = []
    k = []
    dictOfStates = updateState(setOfStates)
    for sk in setOfStates:
        if sk in dictOfStates:
            v += [dictOfStates[sk]]
            k += [sk]
    if len(v) > 0:
        return k[v.index(max(v))]   # min will result in less states in some cases, but longer time execution in others
    else:
        return None


# sends the a function choosing the maximum weight state from provided horizon
def pick(setOfStates):
    return argMax(setOfStates)


# returns the path of the state that provided the solution
def path(state):
    parent = state.parent
    lStates = [state]
    while parent!=None:
        lStates.append(parent)
        parent = parent.parent
    return lStates


# implementation of the breadth-first-search algorithm
def breadth_first_search(game, state0):
    # if the starting state is a final state - return it
    if game.solution(state0):
        return state0
    # sets for horizon and explored states
    horizon = set()
    explored = set()
    # add the first state to the horizon
    horizon.add(state0)
    # while there are still states to check
    while horizon:
        # pick one state from the horizon
        state = pick(horizon)
        # if it is the solution - return the state for printing purpose
        if game.solution(state):
            print("Solution found!")
            print("How many states were explored: " + str(len(explored)))
            return state
        # if it was not yet the solution-add the state to explored
        explored.add(state)
        horizon.remove(state)
        # seek for all possible moves and make them neighboring states
        children = game.neighbors(state)
        # if the neighbor wasn't yet explored add it to the horizon and repeat the loop
        for child in children:
            if (child not in explored) and (child not in horizon):
                horizon.add(child)
    return None


# Main
# those are a few examples with possible to find solutions.
# a 5x5 board with 1 as the smallest number, and 25 as the highest
hidatoBoard1 = [
        [0, 6, 7, 24, 25],
        [0, 0, 0, 22, 0],
        [0, 12, 3, 0, 0],
        [0, 13, 0, 0, 0],
        [14, 0, 1, 0, 0],
    ]
# a 4x4 board with 1 as the smallest number, and 16 as the highest
hidatoBoard2 = [
        [0, 0, 0, 10],
        [14, 16, 0, 11],
        [0, 4, 8, 1],
        [5, 0, 0, 0]
    ]
# a 5x5 board with 1 as the smallest number, and 25 as the highest
hidatoBoard3 = [
        [0, 0, 0, 0, 0],
        [0, 0, 12, 1, 2],
        [16, 0, 0, 10, 25],
        [0, 0, 0, 0, 24],
        [0, 0, 0, 21, 22],
    ]

heuristic = H.HidatoHeuristic()

start_time1 = time.time()

# example number 1
print("This is the first example given board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in hidatoBoard1]))

game1 = G.HidatoGame(hidatoBoard1, 1, 4, 2, heuristic=heuristic)
state0 = game1.getState()
dictOfStates[state0] = heuristic.H(state0)
solution1 = breadth_first_search(game1, state0)

print("This is the winning state board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        for row in solution1.representation.board]))

print("How many steps to the solution: " + str(len(path(solution1))))
print("--- %s seconds ---" % (time.time() - start_time1))

print("---------------------------------------------")
# example number 2
start_time2 = time.time()
print("This is the second example given board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in hidatoBoard2]))

game2 = G.HidatoGame(hidatoBoard2, 1, 2, 3, heuristic=heuristic)
state0 = game2.getState()
dictOfStates[state0] = heuristic.H(state0)
solution2 = breadth_first_search(game2, state0)

print("This is the winning state board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in solution2.representation.board]))

print("How many steps to the solution: " + str(len(path(solution2))))
print("--- %s seconds ---" % (time.time() - start_time2))

print("---------------------------------------------")
# example number 3
start_time3 = time.time()
print("This is the third example given board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in hidatoBoard3]))

game3 = G.HidatoGame(hidatoBoard3, 2, 1, 4, heuristic=heuristic)
state0 = game3.getState()
dictOfStates[state0] = heuristic.H(state0)
solution3 = breadth_first_search(game3, state0)

print("This is the winning state board:")
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in solution3.representation.board]))

print("How many steps to the solution: " + str(len(path(solution3))))
print("--- %s seconds ---" % (time.time() - start_time3))
