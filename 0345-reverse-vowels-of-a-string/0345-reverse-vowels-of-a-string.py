class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # Using a set for faster lookup of vowels
        s = list(s)  # Convert the string to a list to allow mutation
        i, j = 0, len(s) - 1  # Two-pointer approach

        while i < j:
            if s[i] not in vowels:
                i += 1  # Move the left pointer until a vowel is found
            elif s[j] not in vowels:
                j -= 1  # Move the right pointer until a vowel is found
            else:
                s[i], s[j] = s[j], s[i]  # Swap the vowels
                i += 1
                j -= 1

        return ''.join(s)  # Convert list back to string
class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # Using a set for faster lookup of vowels
        s = list(s)  # Convert the string to a list to allow mutation
        i, j = 0, len(s) - 1  # Two-pointer approach

        while i < j:
            if s[i] not in vowels:
                i += 1  # Move the left pointer until a vowel is found
            elif s[j] not in vowels:
                j -= 1  # Move the right pointer until a vowel is found
            else:
                s[i], s[j] = s[j], s[i]  # Swap the vowels
                i += 1
                j -= 1

        return ''.join(s)  # Convert list back to string
