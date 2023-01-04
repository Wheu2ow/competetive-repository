class Solution:
    def isValid(self, s):
        my_dict={'(' : ')', '[' : ']', '{' : '}'}
        stack=[]
        if len(stack) %2!=0 :
                    return False
        for i in s:
            if i in my_dict.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    a=stack.pop()
                    if i!=my_dict[a]:
                        return False
        return stack==[]
        
