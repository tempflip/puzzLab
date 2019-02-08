import math
import random

class WrongMove(Exception):
    pass

def korrekt(size=3):
	x = [i for i in range(1, size**2)]
	x.append(0)
	return tuple(x)

def print_nice(puzz):
	size = int(math.sqrt(len(puzz)))
	for i in range(size) :
		print(puzz[size * i : size * i + size   ])
		pass
	print('...')
		
def move(puzz_, dir, which_el=0):
	puzz = list(puzz_)
	size = int(math.sqrt(len(puzz)))

	ind = puzz.index(which_el)
	
	if (dir == 0): # left
		if (ind % size == 0) : raise(WrongMove("Cant move to left"))
		buff = puzz[ind-1]
		puzz[ind-1] = puzz[ind]
		puzz[ind] = buff

	elif (dir == 1): # right
		if (ind % size == (size-1)) : raise(WrongMove("Cant move to right"))	
		buff = puzz[ind+1]
		puzz[ind+1] = puzz[ind]
		puzz[ind] = buff
	elif (dir == 2): # up
		if (ind < size) : raise(WrongMove("Cant move to up"))	
		buff = puzz[ind-size]
		puzz[ind-size] = puzz[ind]
		puzz[ind] = buff
	elif (dir == 3): # down
		if (ind >= len(puzz)-size) : raise(WrongMove("Cant move to down"))	
		buff = puzz[ind+size]
		puzz[ind+size] = puzz[ind]
		puzz[ind] = buff
	else:
		raise(WrongMove("Dont know what to do"))	

	return tuple(puzz)

def good_move(puzz_, dir, which_el=0):
	try:
		next_state = move(puzz_, dir, which_el)
	except WrongMove:
		return False
	return True

def next_states(puzz):
	states = []
	for mv in range(4):
		if not good_move(puzz, mv) : continue
		states.append(move(puzz, mv))
	return states

def a_to_b(state_a, state_b):
	for mv in range(4):
		if not good_move(state_a, mv) : continue
		if move(state_a, mv) == state_b : return True
	return False


def shuffle(puzz_, steps=5):
	states = [puzz_]
	for i in range(steps):
		success = False
		while not success:
			try:
				next_state = move(states[-1], random.randint(0,3))
				states.append(next_state)
				success = True
			except WrongMove:
				pass
	return states 

random.seed()
