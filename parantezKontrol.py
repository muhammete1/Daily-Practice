"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Bir aritmetik ifadede parantezlerin doğru yerleştirilip yerleştirilmediğini kontrol eden bir program yazın.
"""


class Solution:
    def __init__(self, text):
        self.text = text

    def control(self):
        stack = []
        for i in text:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) <= 0:
                    return False
                elif stack[0] == "(":
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True


# (())
# ()()
# )(
text = "(a+b))((c-2)()"

sol = Solution(text)
print(sol.control())
