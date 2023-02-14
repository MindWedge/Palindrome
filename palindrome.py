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
    
    # checking length is 2 and both characters the same
    if len(word) == 2 and word[0]==word[1]:
        return True
        
    dq = deque(word)

    # checking the characters from the beginning and last
    while len(dq)>2:
        if(dq.popleft().lower())!= dq.pop().lower():
            return False
        
    return True
