#!/python
from puzz import *

pz = korrekt(3)

states = shuffle(pz, steps=7)
for state in states:
	print(state)

print(a_to_b(states[0], states[1]))
print(a_to_b(states[0], states[2]))
print(a_to_b(states[0], states[4]))
print(a_to_b(states[5], states[6]))
print(a_to_b(states[5], states[5]))


print('...........')

print(a_to_b( pz, move(move(move(pz, 0),2),3)   ))


print('xxxxxx...........')
print(next_states(pz))

