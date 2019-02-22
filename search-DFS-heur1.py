from puzz import *
import time
import cProfile
from heapq import *

SIZE = 4
MANHATTAN_MAP = {}
# import heapq
###### depth-first

def heur_simple(correct, state_b): # return the diff between 2 states

	diff_tuple = tuple([a-b != 0 for a, b in zip(correct, state_b)])
	return sum(diff_tuple)

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

# def all_scores(h):
# 	sc = []
# 	for el in h:
# 		sc.append(el[0])
# 	return sc

def main():

	# make up the manhatten map
	for a in range(SIZE**2):
		for b in range(SIZE**2):
			MANHATTAN_MAP[(a,b)] = manhattan_cost(a, b, SIZE)

	goal_pos = korrekt(SIZE)
	# states = shuffle(goal_pos, steps=1000)
	# start_pos = states[-1]

	##### overwrite the start pos!
	#### this is the task


	start_pos = (1, 2, 4, 7, 5, 6, 3, 0, 10, 13, 11, 8, 9, 14, 15, 12)
	# start_pos = shuffle(korrekt(SIZE), steps = 1000)[-1]
	## 
	# start_pos = (0, 1, 5, 4, 3, 2, 7, 8, 6) #10
	# start_pos = (2, 7, 3, 1, 0, 6, 5, 4, 8) #20
	# start_pos = (1, 2, 3, 5, 0, 8, 4, 6, 7) #50

	### 1000
	# start_pos = (1, 4, 7, 3, 5, 8, 0, 2, 6)
	# start_pos = (6, 2, 7, 1, 4, 5, 0, 3, 8)
	# start_pos = (2, 6, 5, 7, 8, 1, 3, 4, 0)
	# start_pos = (2, 7, 4, 8, 6, 5, 3, 1, 0)

	print_nice(start_pos)

	#to_go = [start_pos]
	score_heap = []
	seen = set()
	parent_map = {}
	# score_map = {}
	score_heap = [(0, start_pos)]
	heapify(score_heap)

	start_time = time.time()
	i = 0

	my_heur = heur_manhattan
	# my_heur = heur_simple


	while True:

		# state = to_go.pop()
		(sc, state) = heappop(score_heap)
		print('score', sc)
		# print (all_scores(score_heap))
		seen.add(state)
	 
	 	#### this is the goal
		if (state == goal_pos):
			print('WOOOOOO HOOOO')
			break


		#### generating next states

		# next_states_with_weights = sorted([(state, my_heur(goal_pos, state)) # st, weight
								# for state in next_states(state) # the loop
							# ], key = lambda x: x[1], reverse = True) # sort by weights
		
		# next_sts = [state for state, weight in next_states_with_weights] # get rid of weights

		#### saving the scores for A*
		for next_state in next_states(state):
			# score_map[st] = weight #+ 0*len(route_to(state, start_pos, parent_map))
			if next_state in seen : continue
			heappush(score_heap, (my_heur(goal_pos, next_state), next_state))
			parent_map[next_state] = state # saving the parent, so we can get the route when found the right way

		# next_sts = next_states(state) -- just for testing -- DFS without heuristics


		# for next_state in next_sts:
			# if next_state in seen : continue
			# parent_map[next_state] = state # saving the parent, so we can get the route when found the right way
			# to_go.append(next_state)


		# re-order the queue
		# to_go = sorted(to_go, key = lambda x:score_map[x], reverse = True)

	 	# some output
		i+= 1
		if i % 100 == 0 : print (i)

		# if i > 10 : exit()
	total_time = (time.time() - start_time) * 1000 * 1000

	### get the route
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

# cProfile.run('main()')
main()

