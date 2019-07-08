# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Number of Atoms
# https://leetcode.com/problems/number-of-atoms/

# incomplete, need to finish

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
        char_list = []
        numSeen = False
        inside = False
        string = ""
        inside_counter = 0
        lowerSeen = False
        new_dict = defaultdict(int)

        for i in reverse_list:
            print ("i = ", i)
            if i.isdigit():
                if numSeen:
                    newNum = i + str(num_list[-1])
                    del num_list[-1]
                    num_list.append(int(newNum))
                else:
                    num_list.append(int(i))
                numSeen = True
            # beginning
            elif i == ")":
                inside_counter +=1
                inside = True
                lowerSeen = False
                numSeen = False
                inside_dict = defaultdict(int)
            # end
            elif i == "(":
                print ("inside=", inside_dict)
                print (char_list, num_list)
                print (inside_counter)
            
                if inside_counter > 0:
                    for key, value in inside_dict.items():
                        new_dict[key] += value

                    if len(num_list) > 0:
                        for key, value in new_dict.items():
                            #print (num_list)
                            new_dict[key] *= num_list[-1]
                        del num_list[-1]
                    print new_dict
                else:
                    if len(num_list) > 0:
                        for key, value in inside_dict.items():
                            #print (num_list)
                            inside_dict[key] *= num_list[-1]
                        del num_list[-1]

                    ## merge dictionaries
                    for key, value in inside_dict.items():
                        new_dict[key] += value

                inside_counter -=1

                """
                    if key in new_dict:
                        inside_dict[key] += new_dict.get(key)

                for key, value in new_dict.items():
                    if key not in inside_dict:
                        new_dict[key] = value
                """

                print (inside_dict)
                print (new_dict)

                lowerSeen = False
                numSeen = False
                char_list = []
                inside_dict = defaultdict(int)
                if inside_counter > 0:
                    inside = True
                else:
                    inside = False
                #num_list = []
            elif i.isalpha():
                char = i 
                print (inside, numSeen, lowerSeen)
                print (num_list, char_list)
                # char is lowercased and not seen before
                if char.islower() and not lowerSeen:
                    string = char + string
                    lowerSeen = True
                    continue
                if char.isupper() and lowerSeen:
                    string = char + string
                    lowerSeen = False
                    char = string
                    print (char)
                    string = ""
                    #char_list.append(string)
                if char not in char_list:
                    #print (char_list)
                    char_list.append(char)
                    print (char_list)
                if inside and numSeen and inside_counter > 0:
                    if char not in inside_dict:
                        #print (num_list)
                        inside_dict[char] += num_list[-1]
                        del num_list[-1]
                    else:
                        inside_dict[char] += (num_list[-1])
                        del num_list[-1]
                elif inside and not numSeen and inside_counter > 0:
                    inside_dict[char] += 1
                elif not inside and numSeen:
                    new_dict[char] += num_list[-1]
                else:
                    new_dict[char] += 1
                if len(inside_dict) > 1:
                    print (inside_dict)
                numSeen = False

        print (new_dict)

        new_dict_a = OrderedDict(sorted(new_dict.items(), key=lambda item: item[0], reverse=False))

        string = ""
        for key, value in new_dict_a.items():
            if value > 1:
                #print ("hi")
                string = string + key + str(value)
            else:
                string = string + key

        return string