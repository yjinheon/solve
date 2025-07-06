from re import split
import sys

def add_matrix(matrix_1, matrix_2):

    return [[a+b for a,b in zip(row1,row2)] for row1,row2 in zip(matrix_1, matrix_2)]]



def main():
    lines = sys.stdin.read().splitlines()
    # matrix_size
    n, m = map(int,lines[0].split())
    data = lines[1:]
    matrix_data = [list(map(int,line.split())) for line in data]
    matrix_1 = matrix_data[:n]
    matrix_2 = matrix_data[n:2*n]

    res = add_matrix(matrix_1,matrix_2)
    for row in res:
        print(" ".join(map(str,row)))
    


if __name__ == "__main__":
    main()
