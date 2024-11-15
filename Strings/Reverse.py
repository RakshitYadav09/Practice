def reverse(str):
    
    words = [word for word in str.split('.') if word]
    
    words.reverse()
    
    return '.'.join(words)
