"""

2차원 리스트(행렬)을 90도 회전하는 메소드

"""

def rotate_a_matrix_90(a):
	row_length = len(a)
	col_length = len(a[0])

	res = [[0] * row_length for _ in range(col_length)]

	for r in range(row_length):
		for c in range(col_length):
			res[c][row_length-1-r] = a[r][c]

	return res

