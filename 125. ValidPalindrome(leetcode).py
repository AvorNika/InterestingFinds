class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for sym in s.lower():
            if sym in 'abcdefghijklmnopqrstuvwxyz0123456789':
                new_s.append(sym)

        return new_s == new_s[::-1]