class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

###########################################################

def isInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def good_expression(expression):
    operators = Stack()
    operators.push([])
    for char in range(0, len(expression)):
        if expression[char] == "(":
            operators.push([])
        elif expression[char] == ")":
            if len(operators.top()) == 0 or not "+" in operators.top():
                return False
            operators.pop()
            if not char == len(expression) - 1 and len(operators.top()) > 0:
                if (expression[char + 1] != "x" and expression[char + 1] != "*") and (operators.top()[-1] != "x" and operators.top()[-1] != "*"):
                    return False
            elif not char == len(expression) - 1:
                if expression[char + 1] == "+":
                    return False
            elif len(operators.top()) > 0:
                if operators.top()[-1] == "+":
                    return False
        elif not isInt(expression[char]):
            operators.top().append(expression[char])
    if len(operators.top()) == 0:
        return False
    return True
