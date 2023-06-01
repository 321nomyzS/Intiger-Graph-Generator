from GraphProcessing import *
from GraphVisualization import GraphVisualization
from os import remove, listdir

def main():
    # Get data from file
    with open("../output.txt") as f:
        graphs = f.readlines()

    # Create Matrix Base
    matrix_db = []
    for graph_data in graphs:
        # Process matrix data
        matrix_code = int(graph_data.split(" | ")[0])
        eigenvalues = list(map(int, graph_data.split(" | ")[1].split(" ")[:-1]))
        matrix_size = len(eigenvalues)

        # Generate matrix
        matrix = create_matrix_with_code(matrix_code, matrix_size)

        # Check Connectivity
        if not is_connectivity(matrix):
            continue
        
        # Check if Matrix (or isomorphic Matrix) is in base
        add_bool = True
        for _, matrix_from_base, _ in matrix_db:
            if are_isomorphic(matrix, matrix_from_base):
                add_bool = False  
        if add_bool:
            matrix_db.append((matrix_code, matrix, eigenvalues))

    # Clear graph folder
    files = listdir("./Graph_Processing/graphs")
    for file in files:
        remove("./Graph_Processing/graphs/{}".format(file))

    for matrix_code, matrix, eigenvalues in matrix_db:
        matrix_descrition(matrix_code, matrix, eigenvalues)
        G = GraphVisualization(matrix_code)
        G.add_edges_from_matrix(matrix)
        G.visualize()        

        

if __name__ == "__main__":
    main()
