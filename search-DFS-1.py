from puzz import *
import time
###### depth-first

goal_pos = korrekt(3)
states = shuffle(goal_pos, steps=1)
start_pos = states[-1]
print (states)

print_nice(start_pos)

to_go = [start_pos]
seen = []
# goal_pos_hash = hash(goal_pos)

start_time = time.time()
i = 0
while True:
	state = to_go.pop()
	seen.append(state)
	# print ('State: ', state)
	# print ('Seen: ', seen)
 
	if (state == goal_pos):
		print('WOOOOOO HOOOO')
		break

	for next_state in next_states(state):
		if next_state in seen : continue
		to_go.append(next_state)
		pass
	i+= 1

	print('To go: ',to_go)
	print('........................................')

total_time = (time.time() - start_time) * 1000 * 1000
print ('Iterations: ', i)
print ('Total time: ', total_time)
print ('Avg time / iter: ', int(total_time / i))




