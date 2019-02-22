# Written by Emmit Parubrub on February 22nd, 2019


# this section represents the notes I took from the interview
# ----------------------------------------------------------------------------------------------------------------------
# start - inputString, any sort of arrangement of letters, does not have to be an english word, all lowercases a-z
# end - return a boolean that is true if the string of letters can be rearranged into a palindrome

# aab -> true -> aba
# aabb -> true -> abba or baab
# aaabbb -> false
# aaabbcccc -> true -> bccaaaccb
# racecar -> true
# ----------------------------------------------------------------------------------------------------------------------


# This function checks to see if the input string can be rearranged into a palindrome. If it can, it will return True,
# otherwise it will return false. The function first creates a dictionary of the frequency of occurrences for each
# letter. The function then goes through the dictionary and returns false if there are more than two letters that
# occur an odd number of times.
def palindrome_rearranging(input_string):
    dictionary = word_to_dictionary(input_string)
    num_of_odd_occurrences = 0
    for key in dictionary:
        if dictionary[key] % 2 != 0:
            num_of_odd_occurrences += 1
        if num_of_odd_occurrences > 1:
            return False
    return True


# This function returns a dictionary of the frequency of letter occurrences based upon the input string.
def word_to_dictionary(input_string):
    dictionary = {}
    for letter in input_string:
        keys = dictionary.keys()
        if letter in keys:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary


# This function prints out the results of the palindrome_rearranging function
def test_palindrome_rearranging(input_string):
    if palindrome_rearranging(input_string):
        print(input_string, "is a palindrome")
    else:
        print(input_string, "is NOT a palindrome")


def main():
    test_palindrome_rearranging("aab")
    test_palindrome_rearranging("aabb")
    test_palindrome_rearranging("aaabbb")
    test_palindrome_rearranging("aaabbcccc")
    test_palindrome_rearranging("racecar")


main()
