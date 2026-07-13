class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9 ]', '', s)
        s = s.lower()
        for i, _ in enumerate(s):
            if s[i] != s[len(s)-1-i]:
                print(s[i], s[len(s)-1-i])
                return False
            
            if i >= len(s) / 2:
                break
        
        return True