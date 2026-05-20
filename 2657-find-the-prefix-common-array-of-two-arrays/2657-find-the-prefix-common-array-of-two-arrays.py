from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        res = []

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            res.append(len(seenA & seenB))

        return res