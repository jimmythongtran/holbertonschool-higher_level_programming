#!/usr/bin/python3
def square(num):
    return num * num

def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(0, len(matrix)):
        new_list.append(list(square(num **.5)))
    return (new_list)
    
#    for row in range(0, len(matrix)):
#        for i in range(0, len(matrix[row])):
#           i = (i * i **.5)
#    return matrix
