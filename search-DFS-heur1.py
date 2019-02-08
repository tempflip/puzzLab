from puzz import *
import time
###### depth-first

def heur(correct, state_b):

	diff_tuple = tuple([a-b != 0 for a, b in zip(correct, state_b)])
	return sum(diff_tuple)



goal_pos = korrekt(3)
states = shuffle(goal_pos, steps=60)
start_pos = states[-1]

print_nice(start_pos)

to_go = [start_pos]
seen = []

start_time = time.time()
i = 0
while True:
	state = to_go.pop()
	seen.append(state)
 
	if (state == goal_pos):
		print('WOOOOOO HOOOO')
		break

	next_states_with_weights = sorted([(state, heur(goal_pos, state)) 
							for state in next_states(state)
						], key = lambda x: x[1], reverse = True)
	next_sts = [state for state, weight in next_states_with_weights]

	# print (state)
	# print (next_states_with_weights)

	for next_state in next_sts:
		if next_state in seen : continue
		to_go.append(next_state)

	i+= 1
	if i % 100 == 0 : print (i)

total_time = (time.time() - start_time) * 1000 * 1000
print ('Iterations: ', i)
print ('Total time: ', total_time)
print ('Avg time / iter: ', int(total_time / i))




