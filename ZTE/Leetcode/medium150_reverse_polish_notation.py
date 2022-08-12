"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:
    def evalRPN2(self, tokens):
        ops = set(['+','-','*','/'])
        ctr = 0
        for c in range(len(tokens)):
            if ctr > 0:
                c = c - (ctr*2)
            if tokens[c] in ops:
                res = [str(int(eval(tokens[c-2] + tokens[c] + tokens[c-1])))]
                tokens = tokens[:c-2] + res + tokens[c+1:]
                ctr +=1
        return int(*tokens)

    def evalRPN(self, tokens):
        ops = set(['+','-','*','/'])
        stk = []
        for c in range(len(tokens)):
            if tokens[c] in ops:
                a = stk.pop()
                b = stk.pop()
                stk.append(str(int(eval(b + tokens[c] + a))))
            else:
                stk.append(tokens[c])
        return int(*stk)

if __name__ == "__main__":
    s = Solution()
    tokens = ["2","1","+","3","*"]
    print("1. ", s.evalRPN(tokens))
    tokens = ["4","13","5","/","+"]
    print("2. ", s.evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print("3. ",s.evalRPN(tokens))
