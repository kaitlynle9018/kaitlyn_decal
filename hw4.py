#progress
# 2.1 Creating a List Variable
your_mom = list(range(21))
print(your_mom)

# 2.2 Squaring List Elements
def squareList(lst):
    return [x ** 2 for x in lst]

your_dad = squareList(your_mom)
print(your_dad)

# 2.3 Slicing First 15 Elements
def first_fifteen_elements(lst):
    return lst[:15]

print(first_fifteen_elements(your_dad))

# 2.4 Striding Every 5th Element
def every_fifth_element(lst):
    return lst[4::5]

print(every_fifth_element(your_dad))

# 2.5 Slicing Last 3 Elements & Striding in Reverse
#debug: was getting [324,225,144,81,36,9,0] so I changed the list from lst[-3::-3] to lst[-1:-22:-3]
def fancy_function(lst):
    return lst[-1:-22:-3]

print(fancy_function(your_dad))

# 3.1 Creating a 5x5 2D List
def create_2d_list():
    return [[row * 5 + col + 1 for col in range(5)] for row in range(5)]

matrix = create_2d_list()
print(matrix)

# 3.2 Replacing Multiples of 3 with '?'
def modified_2d_list(matrix):
    return [['?' if num % 3 == 0 else num for num in row] for row in matrix]

new_matrix = modified_2d_list(matrix)
print(new_matrix)

# 3.3 Summing Non-'?' Elements
def sum_non_question_elements(matrix):
    return sum(num if num != '?' else 0 for row in matrix for num in row)

print(sum_non_question_elements(new_matrix))
