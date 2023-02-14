from collections import deque
def is_palindrome(word):
    if not isinstance(word,str):
        raise ValueError("Input value is not a string")
	
	# checking length to be sure more then zero
    if len(word) ==  0:
        return False
    
    # checking length to be sure more then one
    if len(word) == 1:
        return True
        
    return True
