from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    neighbours = []
    if col - 1 >= 0:
        neighbours.append(matrix[row][col - 1])
    if col + 1 < cols:
        neighbours.append(matrix[row][col + 1])
    if row - 1 >= 0:
        neighbours.append(matrix[row - 1][col])
    if row + 1 < rows:
        neighbours.append(matrix[row + 1][col])
    return sorted(neighbours)

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
