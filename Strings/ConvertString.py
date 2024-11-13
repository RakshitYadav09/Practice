# def Convert(string):
#     while True:
#         i = 0
#         while i < len(string):
#             if string[i] == ' ':
#                 string = string[:i] + string[i+1:].capitalize()
#                 break
#             i += 1 
#         if i == len(string):
#             break
#     return string
 
def convert(s):
    if(len(s) == 0):
        return
    s1 = ''
    s1 += s[0].upper()
    for i in range(1, len(s)):
        if (s[i] == ' '):
            s1 += s[i + 1].upper()
            i += 1
        elif(s[i - 1] != ' '):
            s1 += s[i] 
    print(s1)     
    
