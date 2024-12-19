class check_brackets:
    s=[]
    dict={'(':')','[':']','{':'}'}
    def __init__(data):
        for i in dict:
            if i in data:
                i.push(s)
            else:
                s(i.pop())
                return False
        return True
s1=check_brackets()
s1.check_brackets('{[]}')



print('helo world')
print("tata")
