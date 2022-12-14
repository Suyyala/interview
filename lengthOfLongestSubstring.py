def lengthOfLongestSubstring(s):
    # Keep track of the longest substring seen so far
    longest = 0
    # Use a set to keep track of the characters in the current substring
    current = set()
    # Iterate over the characters in the string
    for i in range(len(s)):
        # If the current character is not in the current substring,
        # add it to the current substring and update the longest substring if necessary
        if s[i] not in current:
            current.add(s[i])
            longest = max(longest, len(current))
        # If the current character is in the current substring,
        # remove all of the characters in the current substring up to and including the current character
        # and then add the current character to the current substring
        else:
            while s[i] in current:
                current.remove(s[i])
            current.add(s[i])
    return longest

"""
This solution works by iterating over the characters in the string and keeping track of the longest substring seen so far. It uses a set to keep track of the characters in the current substring, and updates the longest substring if necessary. If the current character is already in the current substring, it removes all of the characters in the current substring up to and including the current character and then adds the current character to the current substring.

The runtime of this solution is O(n), where n is the length of the input string, because the inner loop only runs once for each character in the string. This means that the solution is efficient for long strings.

"""
 

