# Abstractly, vectors are objects that can be added together to form new vectors 
# and that can be multiplied by scalars (i.e., numbers), also to form new vectors.

# Concretely (for us), vectors are points in some finite dimensional space.

# Example vector if we have this data for many people
# [height, age, weight]

from typing import List
Vector = List[float]

height_weight_age = [70, 140, 40]
grades = [95, 80, 75, 62]

# Frequently, we need to add two vectors.
# Vectors add component-wise
# This means if we have the same length vectors v and w
# first element is v[0] + w[0], second element is v[1] + w[1], etc... v[n] + w[n]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


## Similarly, subtracting vectors is a component-wise substraction

def subtract(v: Vector, w: Vector) -> Vector:
    """ subtracts corresponding elements """
    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


# Sum a list of vectors (componentwise)
def vector_sum(vectors: List[Vector]) -> Vector:
    """ Sums all corresponding elements of a list of vectors """
    assert vectors, "no vectors provided!" # make sure that vectors is not empty

    # check that all vectors are the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sized vectors are no good here"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]



def scalar_multiply(c: float, v: Vector) -> Vector:
    """ Multiplies every element by c """
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]



def vector_mean(vectors: List[Vector]) -> Vector:
    """ Computes the element-wise average """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


# Dot product is the sum of the vectors's component-wise products
def dot(v: Vector, w: Vector) -> float:
    """ Computes v_1 * w_1 + ... v_n * w_n """
    assert len(v) == len(w), "vectors must be the same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v: Vector) -> float:
    """ returns v_1 * + v_1 + ... v_n * v_n """
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14


import math

def magnitude(v: Vector) -> float:
    """ Returns the magnitude (or length) of vector v """
    return math.sqrt(sum_of_squares(v)) 

assert magnitude([3, 4]) == 5



def squared_distance(v: Vector, w: Vector) -> float:
    """ computes (v_1 = w_1) **2 ... (x_n - w_n)**2 """
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """ computes the distance between v and w """
    # one way is return math.sqrt(squared_distance(v, w))
    return magnitude(subtract(v, w)) # is probably more clear



# Matrices!
# A matrix is a two dimensional collection of numbers
# If A is a matrix then A[i][j] is the element in the i-th row and j-th column.
# Mathematical notation generally uses capitals to represent matrices

# Another type alias
Matrix = List[List[float]]
 
A = [[1, 2, 3], 
     [4, 5, 6]] # A has 2 rows and 3 columns

B = [[1, 2], 
     [3, 4], 
     [5, 6]] # B has 3 rows


from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """ Returns (# of rows of A, # of columns of A) """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)

# If a matrix has n rows and k columns, we will refer to it as an n × k matrix.
# We can (and sometimes will) think of each row of an n × k matrix as a vector of length k, 
# and each column as a vector of length n:

def get_row(A: Matrix, i: int) -> Vector:
    """ returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    """ returns the j-th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]


from typing import Callable

def make_matrix(
    num_rows: int, 
    num_cols: int, 
    entry_fn: Callable[[int, int, float]]) -> Matrix:
    """ Returns a num_rows by num_cols matrix whose (i, j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)             # given i, create a list
            for j in range(num_cols)]   #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i


def identity_matrix(n: int) -> Matrix:
    """ returns an n by n identity matrix """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [[3, 3, 3], [3, 3, 3], [3, 3, 3]]



# Recall the friendships list of tuples from Chapter 1
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# We could also represent this as:
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

# Consider what it takes to find node's connections...
# We only need to inspect the column or the row corresponding to that node.
friends_of_five = [i 
                    for i, is_friend in enumerate(friend_matrix[5]) if is_friend]

friends_of_five


def get_friends_of_user(user_id: int) -> List:
    return [i for i, is_friend in enumerate(friend_matrix[user_id]) if is_friend]

get_friends_of_user(2)