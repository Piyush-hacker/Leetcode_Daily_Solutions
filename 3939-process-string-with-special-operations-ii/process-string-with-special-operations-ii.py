class Solution:
    def processStr(self, s: str, k: int) -> str:

        length = 0

        for ch in s:

            if 'a' <= ch <= 'z':
                length += 1

            elif ch == '*':
                if length > 0:
                    length -= 1

            elif ch == '#':
                length *= 2

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):

            ch = s[i]

            if 'a' <= ch <= 'z':

                if k == length - 1:
                    return ch

                length -= 1

            elif ch == '#':

                length //= 2
                k %= length

            elif ch == '%':

                k = length - 1 - k

            else:  # '*'

                old_len = length + 1

                if k == old_len - 1:
                    return '.'

                length = old_len

        return '.'