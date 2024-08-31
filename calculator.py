# Program: Calculator 
# author: Manusri Allam
# date: 3/6/2023
'''
# file: Calculator is a program that takes an expression from the user, then does infix to postfix conversion,
makes a tree using stack functionality to organize the various operators and operands. Finally does the calculation
and returns the final answer to the expression. The programn gets advanced by implementing a GUI (a global user interface)
'''
# input: Inputs that are given by the user is the expression to evaluate by the calculator program
# output: It outputs an answer as a float to the given expression provided by the user.

from stack import Stack
import tree
#import stack.py
#Converts the expression from infix to postfix. So basically takes the input as a normal expression
#And then it moves the numbers and operators based on priority.
def infix_to_postfix(infix):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infix 

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#Finally puts all the functions together to calculate the value
def calculate(infix):
    postfix = infix_to_postfix(infix).split()
    answer_tree = tree.ExpTree.make_tree(postfix)
    answer = tree.ExpTree.evaluate(answer_tree)
    return answer



# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    print("Welcome to Calculator Program!")
    x = True
    while x:
        x = input("Please enter your expression here. To quit enter 'quit' or 'q': ")
        try:
            if x == "q" or x == "quit":
                    print("Goodbye!")
                    x = False
            else:
                print(calculate(x))
        except:
            continue
    




    
