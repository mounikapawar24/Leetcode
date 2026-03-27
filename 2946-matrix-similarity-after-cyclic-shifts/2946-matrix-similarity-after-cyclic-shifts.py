class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        shift = k % n   # effective shift

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row -> left shift
                    if mat[i][j] != mat[i][(j + shift) % n]:
                        return False
                else:
                    # odd row -> right shift
                    if mat[i][j] != mat[i][(j - shift + n) % n]:
                        return False

        return True