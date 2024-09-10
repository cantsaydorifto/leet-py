matrices = [40, 20, 30, 10, 30]
# A1 40 x 20
# A2 20 x 30
# A3 30 x 10
# A4 10 x 30


def matrixChainMultiplication(matrices: list[int], i: int, j: int):
    if i == j:
        return 0
    res = float("inf")
    for k in range(i, j):
        res = min(
            matrixChainMultiplication(matrices, i, k)
            + matrixChainMultiplication(matrices, k + 1, j)
            + matrices[i - 1] * matrices[k] * matrices[j],
            res,
        )
