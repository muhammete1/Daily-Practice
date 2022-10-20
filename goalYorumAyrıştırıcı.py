"""
3.04.2022

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
"""

command = "G()(al)"

class Solution:

    def __init__(self, command):
        pass

    def interpret(self):
        return command.replace("()", "o").replace("(al)", "al")


sol = Solution(command)
sol.interpret()
print(sol.interpret())
