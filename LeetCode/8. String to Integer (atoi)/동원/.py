
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = re.compile("(\s*)([+-]?)(\d+)")
        minus = 1
        res = 0
        result = pattern.match(s)
        
        if not result: return 0
        
        if result.group(2) == '-': minus = -1
            
        for c in result.group(3):
            res *= 10
            res += ord(c) - ord('0')

        return max(-2 ** 31, min(res*minus, 2 ** 31 - 1))
