class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # edge cases
        if rows == 1 or not encodedText:
            return encodedText

        n = len(encodedText)
        cols = n // rows   # matrix columns

        # rebuild matrix row-wise
        matrix = [
            encodedText[i * cols:(i + 1) * cols]
            for i in range(rows)
        ]

        # read diagonally (top-left → bottom-right)
        res = []

        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                res.append(matrix[r][c])
                r += 1
                c += 1

        # remove trailing spaces (original text has none)
        return ''.join(res).rstrip()