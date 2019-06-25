# Jenny Huang
# Wallbreakers Cohort #3
# Week 1
# Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, s):
        dictionary = {"A" : 1,
            "B" : 2,
            "C" : 3,
            "D" : 4,
            "E" : 5,
            "F" : 6,
            "G" : 7,
            "H" : 8,
            "I" : 9,
            "J" : 10,
            "K" : 11,
            "L" : 12,
            "M" : 13,
            "N" : 14,
            "O" : 15,
            "P" : 16,
            "Q" : 17,
            "R" : 18,
            "S" : 19,
            "T" : 20,
            "U" : 21,
            "V" : 22,
            "W" : 23,
            "X" : 24,
            "Y" : 25,
            "Z" : 26,
        }

        output = 0
        # determine how many times to multiple based on length of input
        multipler = len(s)-1

        for i in range(len(s)):
            # get all the values before the last value
            if i < (len(s)) and len(s) > 1:
                output = output + 26**(multipler)*dictionary[s[i]]
                multipler = multipler-1
            else:
                output = output + dictionary[s[i]]

        return output