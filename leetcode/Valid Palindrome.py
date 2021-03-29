class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        for i in range(len(strs) // 2):
            if strs[i] != strs[len(strs) - (i + 1)]:
                return False

        return True
