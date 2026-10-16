class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum())
        cleaned = cleaned.lower()
        right = len(cleaned) - 1
        left = 0

        while right >= left:
            if cleaned[right] != cleaned[left]:
                return False
            else:
                right, left = right - 1, left + 1        
        return True