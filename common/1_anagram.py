# Given two strings, check if they are anagrams

from collections import Counter


def check_anagrams_counter(str1: str, str2: str):
    return Counter(str1) == Counter(str2)

def check_anagrams(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    counter1 = {}
    for ch in str1:
        if ch in counter1:
            counter1[ch] +=1
        else:
            counter1[ch] = 1
    
    counter2 = {}
    for ch in str2:
        if ch in counter2:
            counter2[ch] +=1
        else:
            counter2[ch] = 1
    
    for ch, count in counter1.items():
        if ch not in counter2:
            return False
        elif count != counter2[ch]:
            return False
    
    return True
         
