class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        key_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        l = 0
        sub_char = ('I', 'X', 'C')
        sum = 0
        while l < n:
            if l + 1 >= n:
                ch = s[l:]
            else:
                ch = s[l:l+2]
                a = key_dict[ch[0]]
                b = key_dict[ch[1]]
            if len(ch) == 2 and a < b:
                sum += b - a
                l+=2
            else:
                sum += key_dict[ch[0]]
                l+=1
        return sum
    
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
    print(s.romanToInt(""))

