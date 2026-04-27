import re


# Priority of operators
priority = {'+': 1, '-': 1, '*': 2, '/': 2}




# Convert Infix to Postfix
def infix_to_postfix(exp):
   stack = []
   output = []


   for token in exp:
       if token.isalnum():
           output.append(token)
       elif token == '(':
           stack.append(token)
       elif token == ')':
           while stack[-1] != '(':
               output.append(stack.pop())
           stack.pop()
       else:
           while stack and stack[-1] in priority and priority[token] <= priority[stack[-1]]:
               output.append(stack.pop())
           stack.append(token)


   while stack:
       output.append(stack.pop())


   return output




# Generate TAC + Target Code
def generate_code(postfix):
   stack = []
   temp = 1


   print("Three Address Code:")


   for token in postfix:
       if token.isalnum():
           stack.append(token)
       else:
           b = stack.pop()
           a = stack.pop()
           t = f"t{temp}"
           print(f"{t} = {a} {token} {b}")
           stack.append(t)
           temp += 1


   print("\nTarget Code:")
   print("LOAD", stack[-1])
   print("STORE RESULT")




# Infix expression
exp = "a + b * c"


# Tokenize input
tokens = re.findall(r'[a-zA-Z0-9]+|[\+\-\*/\(\)]', exp)


# Convert and generate code
postfix = infix_to_postfix(tokens)


print("Postfix:", ''.join(postfix))
generate_code(postfix)
