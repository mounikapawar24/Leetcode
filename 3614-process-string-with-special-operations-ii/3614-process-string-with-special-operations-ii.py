class Solution:
    def processStr(self, s: str, k: int) -> str:
        LIMIT = 10**15 + 1

        n = len(s)
        lengths = [0] * (n + 1)

        # Forward pass: compute lengths
        for i, ch in enumerate(s):
            cur = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = min(LIMIT, cur + 1)

            elif ch == '*':
                lengths[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lengths[i + 1] = min(LIMIT, cur * 2)

            else:  # '%'
                lengths[i + 1] = cur

        final_len = lengths[n]

        if k >= final_len:
            return '.'

        # Backward pass: trace kth position
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]
            curr_len = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch
                # otherwise character came from previous string

            elif ch == '*':
                # Last character was removed, so positions stay same
                pass

            elif ch == '#':
                if prev_len > 0 and k >= prev_len:
                    k -= prev_len

            else:  # '%'
                if prev_len > 0:
                    k = prev_len - 1 - k

        return '.'