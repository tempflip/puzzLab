#!/python

def korrekt(w=3):
	x = []
	for i in range(w):
		y = []
		for j in range(w):
			y.append(i*w + j + 1)
		x.append(y)
	x[w-1][w-1] = 0
	return x

def print_nice(puzz):
	for i in range(len(puzz)):
		print(puzz[i])
	print('.............................')


def where_is_element(puzz, el=0):
	for i in range(len(puzz)):
		if el in puzz[i]:
			for j in range(len(puzz[i])):
				if (el == puzz[i][j]):
					return (i, j )


def move(puzz, dir, which_el=0):
	
	if (dir == 0): # up
		pos = where_is_element(puzz, which_el) # the 0
		buff = puzz[pos[0]-1][pos[1]]
		puzz[pos[0]-1][pos[1]] = puzz[pos[0]][pos[1]]
		puzz[pos[0]][pos[1]] = buff



	return puzz
	

puzz = korrekt(3)
print_nice(puzz)

puzz = move(puzz, 0, 3)
print_nice(puzz)