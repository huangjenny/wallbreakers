# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # key = letter
        # value = morse code
        morseCodeDictionary = {'a' : ".-",
            'b' : "-...",
            'c' : "-.-.",
            'd' : "-..",
            'e' : ".",
            'f' : "..-.",
            'g' : "--.",
            'h' : "....",
            'i' : "..",
            'j' : ".---",
            'k' : "-.-",
            'l' : ".-..",
            'm' : "--",
            'n' : "-.",
            'o' : "---",
            'p' : ".--.",
            'q' : "--.-",
            'r' : ".-.",
            's' : "...",
            't' : "-",
            'u' : "..-",
            'v' : "...-",
            'w' : ".--",
            'x' : "-..-",
            'y' : "-.--",
            'z' : "--..",
        }      
        
        morseCodeList = []
        for word in words:
            wordList = list(word)
            
            wordString = ""
            # loop through each word in list to create morse code
            for i in range(len(wordList)):
                # use dict to get key of letter to get the morse code
                wordString = wordString + morseCodeDictionary.get(wordList[i])
                
            # append morse code to list    
            morseCodeList.append(wordString)

        return len(set(morsecodeList))