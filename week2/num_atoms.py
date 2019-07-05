# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Number of Atoms
# https://leetcode.com/problems/number-of-atoms/

# todo: incomplete

from collections import defaultdict
from collections import OrderedDict

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        a = formula[::-1] #2)HO(gM       
        reverse_list = list(a)
        num_list = []
        new_dict = defaultdict(int)
        string = ""
        numSeen = False
        char_list = []
        inside = False
        print reverse_list
        for i in reverse_list:
            #print i
            if i.isdigit():
                if numSeen:
                    new_num = i + str(num_list[-1])
                    num_list.append(int(new_num))
                    del num_list[-2]
                else:
                    num_list.append(int(i))
                numSeen = True
            if i == ')': #start
                numSeen = False
                inside = True
                continue
            if i == '(': #end
                print new_dict
                print num_list
                print char_list
                for i in char_list:
                    #print i, num_list[0], new_dict.get(i)
                    #if new_dict.get(i) == 1:
                        #new_dict[i] =  num_list[-1]
                    #else:
                    new_dict[i] *= num_list[-1]
                print new_dict
                numSeen = False
                #char_list = []
                inside = False
                del num_list[-1]
                continue
            if i.isalpha():# and numSeen:
                char = i
                print i, inside, numSeen
                print char_list, num_list
                
                if char.islower():
                    string = char + string
                    continue
                
                if len(string) > 0:
                    string = char + string
                    char = string
                    string = ""
                
                if char not in char_list:
                    char_list.append(char)
                if inside and numSeen:
                    new_dict[char] += num_list[-1]
                    del num_list[-1]
                    numSeen = False
                elif not inside and numSeen:
                    new_dict[char] += num_list[-1]
                    del num_list[-1]
                    numSeen = False
                else:
                    new_dict[char] +=1
                print new_dict
        
        print num_list

        
        print new_dict
        new_dict_a = OrderedDict(sorted(new_dict.items(), key=lambda item: item[0], reverse=False))
        string = ""
        for key, value in new_dict_a.items():
            if value > 1:
                string = string + key + str(value) 
            else:
                string = string + key
        
        print string
        return string
