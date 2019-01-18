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
    '''Returns whether or not a string is a number'''
    try:
        int(n)
        return True
    except ValueError:
        return False

def good_expression(expression):
    '''Returns whether or not an expression is good'''
    #operators is a stack storing all the operators
    operators = Stack()
    operators.push([])
    #plus is a stack storing whether or not each bracket contains a plus
    plus = Stack()
    plus.push(True)
    for char in range(0, len(expression)):
        #If a plus is found the top value for plus should be set to true (to mark that the bracket contains a plus)
        if expression[char] == "+":
            plus.pop()
            plus.push(True)
        #When an open bracket is found, new items are added to each of the stack so that each bracket is given its own node
        if expression[char] == "(":
            operators.push([])
            #By default, it is assumed there is no plus in the bracket
            plus.push(False)
        elif expression[char] == ")":
            #If a bracket contains no operators or no pluses it is redundant
            if len(operators.top()) == 0 or not plus.top():
                return False
            plus.pop()
            operators.pop()
            #If a bracket is not multiplied by anything it is redundant
            if not char == len(expression) - 1 and len(operators.top()) > 0:
                if (expression[char + 1] != "x" and expression[char + 1] != "*") and (operators.top()[-1] != "x" and operators.top()[-1] != "*"):
                    return False
            elif not char == len(expression) - 1:
                if expression[char + 1] == "+":
                    return False
            elif len(operators.top()) > 0:
                if operators.top()[-1] == "+":
                    return False
        #If the character is not a number or a bracket (and therefore an operator), it should be added to the current node in the operator stack
        elif not isInt(expression[char]):
            operators.top().append(expression[char])
    #If the first node in the stack had no operators (and therefore there was a bracket around the entire expression), there were redundant brackets
    if len(operators.top()) == 0:
        return False
    return True
