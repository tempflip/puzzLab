from puzz import *
import time
import cProfile
from heapq import *

SIZE_ = 4
MANHATTAN_MAP = {}
# import heapq
###### depth-first

def heur_manhattan(goal, b, interested):
	score = 0
	for item in b:
		b_pos = b.index(item)
		goal_pos = goal.index(item)
		if interested[goal_pos] == 0 : continue

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

# def all_scores(h):
# 	sc = []
# 	for el in h:
# 		sc.append(el[0])
# 	return sc

def make_manhattan_map(SIZE):
	for a in range(SIZE**2):
		for b in range(SIZE**2):
			MANHATTAN_MAP[(a,b)] = manhattan_cost(a, b, SIZE)

def is_it_the_goal(state, goal_pos, interested):
	match = True
	for i, e in enumerate(goal_pos):
		if interested[i] == 0 : continue
		if e == state[i] : continue
		match = False
	return match

def main():

	goal_pos = korrekt(SIZE_)
	# states = shuffle(goal_pos, steps=1000)
	# start_pos = states[-1]

	##### overwrite the start pos!
	#### this is the task
	start_pos = (1, 9, 8, 7, 14, 15, 6, 0, 5, 12, 3, 11, 4, 13, 10, 2)
	start_pos = (1, 3, 4, 2, 14, 15, 6, 0, 5, 12, 9, 11, 8, 13, 10, 7)
	# start_pos2 = (2, 1, 7, 8, 14, 15, 6, 0, 5, 12, 3, 11, 4, 13, 10, 9)

	# interested =    (1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
	interested =    (1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	# interested =    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1)
	# interested =    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	# interested =    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)	
	# interested =    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)	

	# make_manhattan_map(SIZE_)
	# x = heur_manhattan(start_pos, start_pos2, interested)
	# print(x)
	# exit()

	print_nice(start_pos)
	(path) = find(start_pos, goal_pos, SIZE_, interested)

	print ('Number of states to the solution', len(path))

	print_nice(path[0])


def find(start_pos, goal_pos, SIZE, interested):
	# make up the manhatten map
	make_manhattan_map(SIZE)

	found_pos = None

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
		if (is_it_the_goal(state, goal_pos, interested)):
			found_pos = state
			print('WOOOOOO HOOOO')
			break

		#### saving the scores for A*
		for next_state in next_states(state):
			if next_state in seen : continue
			heappush(score_heap, (my_heur(goal_pos, next_state, interested), next_state))
			parent_map[next_state] = state # saving the parent, so we can get the route when found the right way

		i+= 1
		if i % 1000 == 0 : print (i, sc)

		# if i > 10000 : exit()
	total_time = (time.time() - start_time) * 1000 * 1000

	### get the route
	path = route_to(found_pos, start_pos, parent_map)

	# for st in path:
		# print (st)

	print ('Iterations: ', i)
	print ('Total time: ', total_time)
	print ('Avg time / iter: ', int(total_time / i))

	return (path)

main()

