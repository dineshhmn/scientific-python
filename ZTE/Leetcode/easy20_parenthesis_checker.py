"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class MyStackArr:
    def __init__(self):
        self.value = []

    def lookup(self, val=None):
        if val:
            for idx, a in enumerate(self.value):
                if val == a:
                    return idx
        else:
            print("Check searched value")

    def push(self, val):
        if val:
            self.value.append(val)

    def pop(self):
        return self.value.pop()

    def peek(self):
        if len(self.value) > 0:
            return self.value[-1]
        else:
            return None

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        elif n % 2 != 0:
            return False
        else:
            stk = MyStackArr()
            op_dict = {'(':1,'{':2,'[':3}
            cl_dict = {')':1,'}':2,']':3}
            j = 0
            while j < n:
                if s[j] in op_dict.keys():
                    stk.push(s[j])
                elif s[j] in cl_dict.keys():
                    if op_dict.get(stk.peek()) == cl_dict[s[j]]:
                        stk.pop()
                    else:
                        return False
                j +=1
            if not stk.peek():
                return True
            else:
                return False



if __name__ == "__main__":
    st = Solution()
    s = "()"
    print(st.isValid(s))
    s = "()[]{}"
    print(st.isValid(s))
    s = "((((}}}"
    print(st.isValid(s))
    s = "){"
    print(st.isValid(s))