from puzz import *
import time
import cProfile
from heapq import *

MANHATTAN_MAP = {}

def heur_manhattan(goal, b):
	score = 0
	for item in b:
		if goal.count(item) == 0 : continue

		b_pos = b.index(item)
		goal_pos = goal.index(item)

		### dont calculate, just use the map
		# score += manhattan_cost(b_pos, goal_pos, SIZE)
		score += MANHATTAN_MAP[(b_pos, goal_pos)]
	return score

def is_it_the_goal(state, goal_pos):
	match = True
	for i, e in enumerate(goal_pos):
		if goal_pos[i] == -1 : continue
		if e == state[i] : continue
		match = False
	return match

def route_to(start, goal, parent_map): # calculates the route. Start is the END, so it has to have a parent in the map
	path = [start]
	while path[-1] != goal:
		st = path[-1]
		par = parent_map[st]
		path.append(par)
	return path

def make_manhattan_map(SIZE):
	for a in range(SIZE**2):
		for b in range(SIZE**2):
			MANHATTAN_MAP[(a,b)] = manhattan_cost(a, b, SIZE)

def make_window(puzzle, x, y, window_size):
	pz = []
	puzzle_size = int(math.sqrt(len(puzzle)))
	for i in range(window_size):
		pz += puzzle[    (i+y) * puzzle_size + x : (i+y) * puzzle_size + x + window_size]
	return tuple(pz)


def fix_goal_with_empties(st_p, gl_p_):
	gl_p = list(gl_p_)
	for i in range(len(gl_p)):
		if st_p.count(gl_p[i]) == 0:
			gl_p[i] = -1
	return tuple(gl_p)

def main():
	SIZE_ = 4

	# goal_pos = korrekt(SIZE_)
	# start_pos = (1, 3, 4, 2, 14, 15, 6, 0, 5, 12, 9, 11, 8, 13, 10, 7)

	goal_pos = korrekt(SIZE_)
	states = shuffle(goal_pos, steps=1000)
	start_pos = states[-1]


	print_nice(start_pos)

	window_size = 3
	st_p = make_window(start_pos, 1, 0, window_size)
	gl_p = make_window(goal_pos, 1, 0, window_size)

	print_nice(st_p)
	print_nice(gl_p)

	gl_p = fix_goal_with_empties(st_p, gl_p)

	print_nice(gl_p)

	(path) = find(st_p, gl_p)

	print ('Number of states to the solution', len(path))

	print_nice(path[0])


def find(start_pos, goal_pos):
	# make up the manhatten map
	make_manhattan_map(int(math.sqrt(len(start_pos)))) # -> size of the puzzle

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
		if (is_it_the_goal(state, goal_pos)):
			found_pos = state
			print('WOOOOOO HOOOO')
			break

		#### saving the scores for A*
		for next_state in next_states(state):
			if next_state in seen : continue
			heappush(score_heap, (my_heur(goal_pos, next_state), next_state))
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

