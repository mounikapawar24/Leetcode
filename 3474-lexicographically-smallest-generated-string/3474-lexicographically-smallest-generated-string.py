class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # Python 3
        n, m = len(str1), len(str2)
        L = n + m - 1

        # Start with smallest lexicographic string
        word = ['a'] * L

        # ---------------------------------------------------
        # 1. Force all 'T' constraints
        # ---------------------------------------------------
        forced = [False] * L

        for i, ch in enumerate(str1):
            if ch == 'T':
                for j in range(m):
                    pos = i + j
                    if forced[pos] and word[pos] != str2[j]:
                        return ""
                    word[pos] = str2[j]
                    forced[pos] = True

        # ---------------------------------------------------
        # 2. Build KMP prefix table for str2
        # ---------------------------------------------------
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and str2[i] != str2[j]:
                j = lps[j - 1]
            if str2[i] == str2[j]:
                j += 1
                lps[i] = j

        # helper: check equality with str2 at index i
        def matches(i):
            for j in range(m):
                if word[i + j] != str2[j]:
                    return False
            return True

        # ---------------------------------------------------
        # 3. Fix 'F' constraints (must NOT match str2)
        #    Greedily modify rightmost possible character
        # ---------------------------------------------------
        for i, ch in enumerate(str1):
            if ch == 'F' and matches(i):

                changed = False

                # try changing from right → left
                for j in range(m - 1, -1, -1):
                    pos = i + j

                    if forced[pos]:
                        continue

                    # increase character minimally
                    for c in range(ord(word[pos]) + 1, ord('z') + 1):
                        word[pos] = chr(c)
                        changed = True
                        break

                    if changed:
                        break

                if not changed:
                    return ""

        # ---------------------------------------------------
        # 4. Final validation (safety check)
        # ---------------------------------------------------
        for i, ch in enumerate(str1):
            ok = True
            for j in range(m):
                if word[i + j] != str2[j]:
                    ok = False
                    break

            if (ch == 'T' and not ok) or (ch == 'F' and ok):
                return ""

        return "".join(word)