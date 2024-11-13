def Convert(string):
    while True:
        i = 0
        while i < len(string):
            if string[i] == ' ':
                string = string[:i] + string[i+1:].capitalize()
                break
            i += 1 
        if i == len(string):
            break
    return string
 