# @ SionaRavi
# This program prompts for and evaluates a prefix expression.

# Returns True if the given string can be converted
# into a float successfully, or False if not.
def is_float(s):
try:
num=float(s)
return True
except:
return False
# pre : operator is one of +, -, *, /, or % (this is the list of valid operators)
# post: returns the result of applying the given operator
# to the given operands
# if you encounter an operator that is not in the list of valid ones,
# raise a ValueError with the message "bad operator" followed by the operator
def apply(operator, operand1, operand2):
if operator in "+-*/%":
if operator=="+":
return operand1+operand2
if operator=="-":
return operand1-operand2
if operator=="*":
return operand1*operand2
if operator=="/":
return operand1/operand2
if operator=="%":
return operand1%operand2
   raise ValueError("bad operator "+operator)
# pre : tokens is a list that represents a legal prefix expression
# post: expression is evaluated and the result is returned
# NOTE: this recursive function is complete and works as indicated by pre and post conditions
def evaluate(tokens):
# extract first token from the list
first = tokens.pop(0)
if is_float(first):
# base case: a numeric token
return float(first)
else:
# recursive case: an operator
operand1 = evaluate(tokens)
operand2 = evaluate(tokens)
return apply(first, operand1, operand2)

def main():
print("This program evaluates prefix expressions that")
print("include the operators +, -, *, /, and %.")
print()
# ask user to enter a prefix expression
expr = input("Prefix expression? ")
# repeat until expression entered is blank
while expr != "quit":
# split input line into tokens and store in a list called tokens
tokens=expr.split(" ")
value = evaluate(tokens) # calls the recursive function which evaluates the expression contained in the list tokens
print("value =", round(value, 2)) # outputs the expression's value
# get another prefix expression from the user
expr = input("Prefix expression? ")
print("Exiting.")

main()
    # ask user to enter a prefix expression
    expr = input("Prefix expression? ")
    # repeat until expression entered is blank
    while expr != "quit":
        # split input line into tokens and store in a list called tokens

        value = evaluate(tokens) # calls the recursive function which evaluates the expression contained in the list tokens

        print("value =", round(value, 2)) # outputs the expression's value

        # get another prefix expression from the user

    print("Exiting.")

main()
