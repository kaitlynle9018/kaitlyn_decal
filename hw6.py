import numpy as np
#Section 1: Prime Clusters
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    mask = np.apply_along_axis(lambda row: any(is_prime(x) for x in row), axis=1, arr=arr)
    return arr[mask]

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsPrimes(arr))

#Section 2: Let's Play Checkers
#2.1: Matrix with only 0s
def checkerboard_zeros():
    return np.zeros((8, 8), dtype=int)

print(checkerboard_zeros())

#2.2: Matrix with Odd rows
def checkerboard_odd_rows():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  
    return board

print(checkerboard_odd_rows())

#2.3: Matrix with even rows
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  
    board[1::2, 1::2] = 1  
    return board

print(checkerboard())
#2.4: Reverse checkerboard
def reverse_checkerboard():
    board = np.ones((8, 8), dtype=int)
    board[::2, ::2] = 0
    board[1::2, 1::2] = 0
    return board
print(reverse_checkerboard())
#Section 3: Expanding Universe
def expansion(strings, spaces):
    return np.array([" ".join(list(s)).replace(" ", " " * spaces) for s in strings])


universe = np.array(["galaxy", "clusters"])
print(expansion(universe, 1))

#Section 4: Second-Dimmest Star
def secondDimmest(stars):
    sorted_stars = np.sort(stars, axis=0)
    return sorted_stars[1, :]
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))
