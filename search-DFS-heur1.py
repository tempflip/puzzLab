from puzz import *
import time
###### depth-first

def heur_simple(correct, state_b): # return the diff between 2 states

	diff_tuple = tuple([a-b != 0 for a, b in zip(correct, state_b)])
	return sum(diff_tuple)

def heur_manhattan(goal, b):
	score = 0
	for item in b:
		b_pos = b.index(item)
		goal_pos = goal.index(item)

		score += manhattan_cost(b_pos, goal_pos, SIZE)
	return score


goal_pos = korrekt(3)
# states = shuffle(goal_pos, steps=60)
# start_pos = states[-1]

##### overwrite the start pos!
#### this is the task
SIZE = 3

# start_pos = (1, 2, 4, 7, 5, 6, 3, 0, 10, 13, 11, 8, 9, 14, 15, 12)
## 
# start_pos = (0, 1, 5, 4, 3, 2, 7, 8, 6) #10
start_pos = (2, 7, 3, 1, 0, 6, 5, 4, 8) #20
# start_pos = (1, 2, 3, 5, 0, 8, 4, 6, 7) #50

print_nice(start_pos)

to_go = [start_pos]
seen = []
parent_map = {}

start_time = time.time()
i = 0

my_heur = heur_manhattan
# my_heur = heur_simple

while True:
	state = to_go.pop()
	print ('###', state, my_heur(goal_pos, state))

	seen.append(state)
 
	if (state == goal_pos):
		print('WOOOOOO HOOOO')
		break

	next_states_with_weights = sorted([(state, my_heur(goal_pos, state)) # st, weight
							for state in next_states(state) # the loop
						], key = lambda x: x[1], reverse = True) # sort by weights
	next_sts = [state for state, weight in next_states_with_weights] # get rid of weights


	# next_sts = next_states(state) -- just for testing -- DFS without heuristics
	# print (state)
	# print (next_states_with_weights)

	for next_state in next_sts:
		if next_state in seen : continue
		parent_map[next_state] = state # saving the parent, so we can get the route when found the right way
		to_go.append(next_state)

	i+= 1
	if i % 100 == 0 : print (i)

total_time = (time.time() - start_time) * 1000 * 1000

### get the route
path = [goal_pos]
while path[-1] != start_pos:
	st = path[-1]
	par = parent_map[st]
	# print(a_to_b(st, par))
	# print (path[-1])
	path.append(par)


# print(parent_map)

print ('Iterations: ', i)
print ('Total time: ', total_time)
print ('Avg time / iter: ', int(total_time / i))



print ('Number of states to the solution', len(path))
#for state in path:
#	print (state)




