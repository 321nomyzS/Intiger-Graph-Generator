def create_permutations(j, P, permutations):
    if j == 0:
        permutations.append(P.copy())
    else:
        for i in range(j):
            P[i], P[j - 1] = P[j - 1], P[i]
            create_permutations(j - 1, P, permutations)
            P[i], P[j - 1] = P[j - 1], P[i]

def create_temporary_matrix(permutation, matrixB):
    n = len(matrixB)
    temporaryMatrix = list()
    for i in range(n):
        temp = list()
        for j in range(n):
            temp.append(0)
        temporaryMatrix.append(temp)
    for i in range(n):
        for j in range(n):
            temporaryMatrix[permutation[i]][permutation[j]] = matrixB[i][j]
    return temporaryMatrix

def compare_matrix(matrixA, temporaryMatrix):
    n = len(matrixA)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if temporaryMatrix[i][j] != matrixA[i][j]:
                return False
    return True

def are_isomorphic(matrixA, matrixB):
    n = len(matrixA)
    P = list(range(n))
    permutations = list()
    create_permutations(n, P, permutations)
    isomorphic = False
    for permutation in permutations:
        temporaryMatrix = create_temporary_matrix(permutation, matrixB)
        if compare_matrix(matrixA, temporaryMatrix):
            isomorphic = True
            break

    return isomorphic

def DFS(matrix, start, visited):
    visited[start] = True
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and not visited[i]:
            DFS(matrix, i, visited)

def is_connectivity(matrix):
    visited = [False] * len(matrix)
    DFS(matrix, 0, visited)
    for i in range(len(visited)):
        if not visited[i]:
            return False
    return True

def create_matrix_with_code(matrix_code, matrix_size):
    triangle_size = matrix_size * (matrix_size - 1) // 2
    binary_code = decimal_to_bin(matrix_code, triangle_size)

    result_matrix = []
    for _ in range(matrix_size):
        result_matrix.append([0] * matrix_size)
    
    k = 0
    for i in range(matrix_size):
        for j in range(i+1, matrix_size):
            result_matrix[i][j] = binary_code[k]
            result_matrix[j][i] = binary_code[k]
            k += 1

    return result_matrix

def decimal_to_bin(decimal, size):
    index = size - 1

    result_list = [0] * size

    while decimal > 0:
        result_list.append(decimal % 2)
        decimal = int(decimal / 2)
    
    result_list.reverse()
    return result_list

def matrix_descrition(matrix_code, matrix, eigenvalues):

    # # Matrix reprezentation
    # result_str = "$\n\\begin{bmatrix}\n"
    # lines_format = []
    # for line in matrix:
    #     lines_format.append(" & ".join(map(str, line)))
    
    # result_str += " \\\\\n".join(lines_format)
    # result_str += "\n\end{bmatrix}\n$\n"
    print("Macierz numer:", matrix_code)
    for line in matrix:
        print(line)
    print("Wartości własne:", eigenvalues)
    print()
