'''This program will convert text from the 'InputMatrices' text file into proper MATLAB-formatted code for a matrix. See the readme file for more.'''

input_matrix = open("InputMatrices.txt", "r")
matrix = input_matrix.read().rstrip()
matrix = matrix.split("\n")
input_matrix.close()

for row in range(len(matrix)):
    matrix[row] = matrix[row].split("\t")

output_string = ""

for index, row in enumerate(matrix):
    for column, value in enumerate(row):
        output_string += value

        if column < len(row) - 1:
            output_string += ", "

    output_string += ";"
    if index < len(matrix) - 1:
        output_string += "\n"

output_matrix = open("OutputMatrices.txt", "w")
output_matrix.write("[" + output_string + "]")
output_matrix.close()
