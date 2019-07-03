# Jenny Huang
# Wallbreakers Cohort #3
# Week 2
# Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/

from collections import defaultdict

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # key = domain list
        # value = domain value       
        cpdomains_dict = defaultdict(int)
        
        for domain in cpdomains:
        	# split at the space to separate the domain value and domain list
            domain_list = list(domain.split())

            domain_value = int(domain_list[0])
            domain_only = domain_list[1]
            # insert first domain value into dictionary
            if domain_only in cpdomains_dict.keys():
                cpdomains_dict[domain_only] += domain_value
            else:
                cpdomains_dict[domain_only] = domain_value

            # split at the '.'
            split_domain = domain_only.split(".")
            
            # look at the rest of the subdomains
            for subdomain in range(1,len(split_domain)):
                new_list = split_domain[subdomain::]

                string = ""
                # build subdomain strings
                for i in range(len(new_list)):
                    if new_list[i] == new_list[-1]:
                        string = string + new_list[i]
                    else:
                        string = string + new_list[i] + "."

                # clean up subdomain strings
                if string in cpdomains_dict.keys():
                    cpdomains_dict[string] += domain_value
                else:
                    cpdomains_dict[string] = domain_value
        
        cpdomains_list = []
        string = ""
        # convert dictionary to list
        for key, value in cpdomains_dict.items():
            string = str(value) + " " + str(key)
            cpdomains_list.append(string)

        return cpdomains_list