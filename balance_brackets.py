def check_balance_brackets(strlist): 
    string = strlist
    stack=[]
    if string =='' or len(string)%2!=0:
        return False
    else:
        try:
            for i in range(0,len(string)):
                if string[i]=='{' or string[i]=='[' or string[i]=='(':
                    stack.append(string[i])
                else:
                    if stack[-1]=='(' and string[i] ==')':
                        stack.pop()
                    elif stack[-1]=='[' and string[i] ==']':
                        stack.pop()
                    elif stack[-1]=='{' and string[i] =='}':
                        stack.pop()
                    else:
                        return False
                    
            return True     
        except Exception as e:
            return False
                
# enter the brackets here to check its balanced or not                
if check_balance_brackets('{[[]]}') :
    print('balanced brackets')
else:
    print('un-balanced brackets')
