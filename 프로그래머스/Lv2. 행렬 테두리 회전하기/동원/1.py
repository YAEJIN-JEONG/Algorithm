def solution(rows, columns, queries):
    matrix = [[columns * (i - 1) + j for j in range(columns + 1)] 
             for i in range(rows + 1)]
    return [shift_and_return_min(matrix, query) for query in queries]

def shift_and_return_min(matrix, query):
    idxs = get_idxs(*query)
    values = [matrix[x][y] for (x, y) in idxs]
    for ((x, y), value) in zip(idxs, values[-1:] + values[:-1]):
        matrix[x][y] = value
    return min(values)
    
def get_idxs(x1, y1, x2, y2):
    return [(x1, y) for y in range(y1, y2 + 1)] + \
           [(x, y2) for x in range(x1, x2 + 1)][1:] + \
           [(x2, y) for y in range(y2, y1 - 1, -1)][1:] + \
           [(x, y1) for x in range(x2, x1 - 1, -1)][1:-1]
