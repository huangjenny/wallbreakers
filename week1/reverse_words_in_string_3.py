# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Reverse Words in a String 3
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution(object):
    def reverseWords(self, s):
        # list to store reversed string        
        stringList = list(s)
        
        for i in range(len(stringList)/2):
            # save first and last letters in variables
            lastLetter = stringList[len(stringList)-1-i]
            firstLetter = stringList[i]
            
            # swap letters
            stringList[i] = lastLetter
            stringList[len(stringList)-1-i] = firstLetter
        
        newString = ''.join(stringList)
        
        newString1 = newString.split()
        newString1.reverse()
        newString2 = ' '.join(newString1)

        return newString2