from puzz import *
import time
###### depth-first

goal_pos = korrekt(3)
states = shuffle(goal_pos, steps=5)
start_pos = states[-1]
print (states)

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

	for next_state in next_states(state):
		if next_state in seen : continue
		to_go.append(next_state)

	i+= 1
	if i % 100 == 0 : print (i)

total_time = (time.time() - start_time) * 1000 * 1000
print ('Iterations: ', i)
print ('Total time: ', total_time)
print ('Avg time / iter: ', int(total_time / i))




