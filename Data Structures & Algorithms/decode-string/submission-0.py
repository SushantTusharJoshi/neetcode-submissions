class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        cur = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)

            elif ch == "[":
                stack.append((cur, k))
                cur = ""
                k = 0

            elif ch == "]":
                prev, num = stack.pop()
                cur = prev + cur * num

            else:
                cur += ch

        return cur
        