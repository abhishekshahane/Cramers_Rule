"""
This program will calculate the solution for a system of equations with three variables(given three equations) using 
Cramer's rule.
"""
import numpy as np
from numpy import linalg
# Globals - also column vector is I think what it's called
column_vector = []
total_matrix = []
def determinant(x):
    # I'm not about to write a determinant function myself when numpy exists
    return linalg.det(np.array(x))
def get_input():
    for i in range(3):
        a = input("Enter a equation: ")
        b = a.split("=")
        column_vector.append(int(b[1].strip(" ")))
        # Get the relevant coefficients
        c = b[0].replace(" ", "").replace("x",",").replace("y", ",").replace("z","").replace("+","")
        values = c.split(",")
        total_matrix.append([int(value) for value in values])
    return [total_matrix, column_vector]
d_container = get_input()
# I'm definitely sure that there's a better way to do this, but meh
dx = [
    [d_container[1][0], d_container[0][0][1], d_container[0][0][2]],  
    [d_container[1][1], d_container[0][1][1], d_container[0][1][2]],
    [d_container[1][2], d_container[0][2][1], d_container[0][2][2]]
    ]
det_dx = determinant(dx)
dy = [
    [d_container[0][0][0], d_container[1][0], d_container[0][0][2]],
    [d_container[0][1][0], d_container[1][1], d_container[0][1][2]],
    [d_container[0][2][0], d_container[1][2], d_container[0][2][2]]
]
det_dy = determinant(dy)
dz =  [
    [d_container[0][0][0], d_container[0][0][1], d_container[1][0]], 
    [d_container[0][1][0], d_container[0][1][1], d_container[1][1]],
    [d_container[0][2][0], d_container[0][2][1], d_container[1][2]]
]
det_dz = determinant(dz)
det_d = determinant(d_container[0])
if det_d == 0:
    print("Sorry, either this system of equations has infinite solutions or has none.")
else:
    print("X: ", int(det_dx/det_d))
    print("Y: ", int(det_dy/det_d))
    print("Z: ", int(det_dz/det_d))
