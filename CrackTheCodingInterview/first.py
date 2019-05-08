

def first_question(string):
    """Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
    """
    hash = dict()
    flag = True
    for s in string:
        if s not in hash:
            hash[s] = True
        else:
            flag = False
        if flag == False:
            break
    return flag


def second_question(string):
    """Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character )
    """
    return string[::-1]


def third_question(string):
    """Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer NOTE: One or two additional variables are fine An extra copy of the array is not

    FOLLOW UP
    Write the test cases for this method
    """
    string = list(string)
    swaps = True
    length = len(string)
    special_key = "#"
    for i in range(length):
        for j in range(i+1, length):
            if string[i] == special_key:
                break
            else:
                if string[i] == string[j]:
                    string[j] = special_key
    return ''.join(string).replace(special_key, '')


def fourth_question(string1, string2):
    """Write a method to decide if two strings are anagrams or not"""
    from collections import Counter
    if Counter(string1) == Counter(string2):
        return True
    else:
        return False


def fifth_question(string):
    return string.replace(" ", "%20")


def sixth_question(matrix):
    m, n = len(matrix), len(matrix[0])
    mid = int(m / 2)
    for level in range(0, mid):
        first = level
        last = n - 1 - level
        for offset in range(first, last):
            # rotation of values
            points = (matrix[first][first + offset], matrix[first + offset][last], matrix[last][last - offset],
                      matrix[last - offset][first])
            # print(points , points[1:] + points[:1])
            (matrix[first][first + offset], matrix[first + offset][last], matrix[last][last - offset],
             matrix[last - offset][first]) = (points[-1], points[0], points[1], points[2])

def seventh_queston(matrix):
    """"""
    pass


def eight_question(string1, string2):
    """Assume you have a method isSubstring which checks if one word is a substring of another Giventwostrings,s1ands2,write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”)"""
    def is_substring(s1, s2):
        return s1 in s2
    # first check if length is same
    # second say if s2 is '345012', concatenate it with itself ==> '345012' + '345012' ==> '345012345012'
    # Now check if S1 which '012345' is a substring of s2s2
    return len(string1) == len(string2) and is_substring(string1, string2 + string2)

