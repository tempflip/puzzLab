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

def where_is_element(puzz, el):
	for i in range(len(puzz)):
		if el in puzz[i]:
			for j in range(len(puzz[i])):
				if (el == puzz[i][j]):
					return (i, j )


# def move(where):
# 	if (where == 0):

# 	else if 

puzz = korrekt(3)
print(where_is_element(puzz, 0))