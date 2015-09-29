import re
def is_anagram(a, b):
    a_l = a.lower()
    b_l = b.lower()
    s1 = ''.join(re.findall(r"[\w]+",a_l))
    s2 = ''.join(re.findall(r"[\w]+",b_l)) 
    if len(s1) != len(s2):
        return False
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list.sort()
    s2_list.sort()
#    print s1_list
#    print s2_list
    if s1_list == s2_list:
        return True
    return False

#print is_anagram("hi, i am prachi! :)", "chIPH ar , , ,I?ami")
