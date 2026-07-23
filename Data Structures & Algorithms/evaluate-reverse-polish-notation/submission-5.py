class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[0]
        operators = {'+','-','*','/'}

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            if i in operators:
                b= stack.pop()
                a= stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*" :
                    stack.append(a*b)
                elif i == "/":
                    stack.append(int(a/b))
        return stack[-1]


            