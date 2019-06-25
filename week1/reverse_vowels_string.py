# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):  
    def reverseVowels(self, s):
        # create list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        listS = list(s)
        vowelsList = []
        
        # create a list of vowels from string
        for i in listS:
            if i in vowels:
                vowelsList.append(i)
        
        # replace vowels in string with reversed vowel list
        vowelsList.reverse()
        pointer = 0 # pointer for vowelsList list
        for i in range(len(listS)):
            if listS[i] in vowels:
                listS[i] = vowelsList[pointer]
                pointer = pointer + 1 # increment pointer
                
        reversedVowelString = ''.join(listS)     
        
        return reversedVowelString 