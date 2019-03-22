from puzz import *
import time
import cProfile
from heapq import *

SIZE = 4
MANHATTAN_MAP = {}

# def heur_simple(correct, state_b): # return the diff between 2 states

# 	diff_tuple = tuple([a-b != 0 for a, b in zip(correct, state_b)])
# 	return sum(diff_tuple)

def heur_manhattan(goal, b):
	score = 0
	for item in b:
		b_pos = b.index(item)
		goal_pos = goal.index(item)

		### dont calculate, just use the map
		# score += manhattan_cost(b_pos, goal_pos, SIZE)
		score += MANHATTAN_MAP[(b_pos, goal_pos)]
	return score

def route_to(start, goal, parent_map): # calculates the route. Start is the END, so it has to have a parent in the map
	path = [start]
	while path[-1] != goal:
		st = path[-1]
		par = parent_map[st]
		path.append(par)
	return path

def main():

	# make up the manhatten map
	for a in range(SIZE**2):
		for b in range(SIZE**2):
			MANHATTAN_MAP[(a,b)] = manhattan_cost(a, b, SIZE)

	goal_pos = korrekt(SIZE)
	states = shuffle(goal_pos, steps=1000)
	start_pos = states[-1]

	##### overwrite the start pos!
	#### this is the task

	print_nice(start_pos)

	score_heap = []
	seen = set()
	parent_map = {}
	score_heap = [(0, start_pos)]
	heapify(score_heap)

	start_time = time.time()
	i = 0

	my_heur = heur_manhattan


	while True:
		(sc, state) = heappop(score_heap)
		seen.add(state)
	 
	 	#### this is the goal
		if (state == goal_pos):
			print('WOOOOOO HOOOO')
			break

		#### saving the scores for A*
		for next_state in next_states(state):
			if next_state in seen : continue
			heappush(score_heap, (my_heur(goal_pos, next_state), next_state))
			parent_map[next_state] = state # saving the parent, so we can get the route when found the right way

	 	# some output
		i+= 1
		if i % 1000 == 0 : print (i, sc)

	total_time = (time.time() - start_time) * 1000 * 1000

	### get the routes
	# print (parent_map)
	path = route_to(goal_pos, start_pos, parent_map)

	# for st in path:
		# print (st)

	print ('Iterations: ', i)
	print ('Total time: ', total_time)
	print ('Avg time / iter: ', int(total_time / i))



	print ('Number of states to the solution', len(path))
	#for state in path:
	#	print (state)

main()

