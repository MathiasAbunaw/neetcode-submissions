class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        for i in range(len(s) -1, -1, -1):
            rev += s[i]
        rev = re.sub(r'[^a-zA-z0-9]','', rev)
        s = re.sub(r'[^a-zA-z]','', s)
        print(rev)
        if rev.lower() == s.lower():
            return True;
        else:
            return False