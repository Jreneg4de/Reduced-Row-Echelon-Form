import numpy as np

def rref(matrix):
    lead = 0
    row_count, col_count = matrix.shape

    for r in range(row_count):
        if col_count <= lead:
            break
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if col_count == lead:
                    return

        matrix[i], matrix[r] = matrix[r], matrix[i]

        lv = matrix[r][lead]
        matrix[r] = matrix[r] / lv
        for i in range(row_count):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = matrix[i] - lv * matrix[r]
        lead += 1

    return matrix

def validate_matrix(matrix_str):
    rows = matrix_str.split(';')
    num_rows = len(rows)
    num_cols = len(rows[0].split())

    for row in rows:
        elements = row.split()
        if len(elements) != num_cols:
            raise ValueError("Inconsistent number of elements in each row.")
        for element in elements:
            try:
                float(element)
            except ValueError:
                raise ValueError("Invalid matrix element: {}".format(element))

    return num_rows, num_cols

def main():
    while True:
        print("Enter the matrix elements row by row, separated by spaces.")
        print("Use semicolons (;) to separate rows.")
        print("Example: 1 2 3; 4 5 6; 7 8 9")
        print("Enter 'q' to quit.")

        matrix_str = input("Matrix: ")

        if matrix_str.lower() == 'q':
            break

        try:
            num_rows, num_cols = validate_matrix(matrix_str)
            matrix = np.array([list(map(float, row.split())) for row in matrix_str.split(';')])
            print("\nOriginal Matrix:")
            print(matrix)

            rref_matrix = rref(matrix.copy())
            print("\nReduced Row Echelon Form (RREF):")
            print(rref_matrix)
            print()

        except ValueError as e:
            print("Error:", str(e))
            print()

if __name__ == '__main__':
    main()