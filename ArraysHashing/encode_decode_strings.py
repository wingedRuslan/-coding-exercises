""" 
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
"""


class Solution:
    """
    Tricky Part - in input strings in list contain any possible character
    How to create a delimiter between each word? how to know where one ends and another begins?
    
    Idea: ['apple', 'pen'] --> '5@apple' + '3@pen' --> encoded representation

    Time: O(n)
    n - total number of chars in the list of words
    """
	
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        
        encoded_res = ''
        for s in strs:
            encoded_res += str(len(s)) + '@' + s
        
        return encoded_res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        
        decoded_list = []
		
        i = 0
		
        while i < len(s):
            
            # find the delimiter - the end of the integer
            # integer - the length of next word 
            j = i
            while s[j] != '@':
                j += 1
            
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            decoded_list.append(word)

            i = j + 1 + length

        return decoded_list


