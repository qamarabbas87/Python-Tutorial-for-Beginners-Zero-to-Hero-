#Level 3: Strings (building results)
#Reverse a string
#Input: string s
#Output: reversed string
def ReverseString(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str 
print(ReverseString("Hello World"))
print(ReverseString("Python Programming"))


#############################################################################################
#Palindrome check
#Input: string s
#Output: True/False (ignore spaces optional later)
def IsPalindrome(s):
    cleaned_s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return cleaned_s == cleaned_s[::-1]  # Check if cleaned string is equal to its reverse

print(IsPalindrome("A man a plan a canal Panama"))
print(IsPalindrome("Hello World"))          


###############################################################################################
#Remove duplicates (keep order)
#Input: string s
#Output: string with first occurrences only
def RemoveDuplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)      
print(RemoveDuplicates("hello world icecream world!"))
print(RemoveDuplicates("python programming"))

#Count words
#Input: string s    
#Output: number of words (split by spaces)
def CountWords(s):
    words = s.split()
    return len(words)       
print(CountWords("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(CountWords("Python Programming is fun!"))

#Longest word
#Input: string s    
#Output: longest word (split by spaces)
def LongestWord(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(LongestWord("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(LongestWord("Python Programming is fun!"))

#Count vowels and consonants
#Input: string s
#Output: number of vowels and consonants
def CountVowelsAndConsonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    vowel_list = []
    consonant_list = []

    for char in s:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
                vowel_list.append(char)
            else:
                consonant_count += 1
                consonant_list.append(char) 
    return vowel_count, consonant_count, vowel_list, consonant_list     
print(CountVowelsAndConsonants("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(CountVowelsAndConsonants("Python Programming is fun!"))

#Anagram check
#Input: strings s1, s2  
#Output: True/False (ignore spaces and case)
def AreAnagrams(s1, s2):
    cleaned_s1 = s1.replace(" ", "").lower()
    cleaned_s2 = s2.replace(" ", "").lower()
    return sorted(cleaned_s1) == sorted(cleaned_s2)  # Check if sorted characters are the same
print(AreAnagrams("Listen", "Silent"))
print(AreAnagrams("Hello World", "World Hello"))
print(AreAnagrams("Python", "Java"))

print('sorted list is ' + str(sorted("Listen qamar abbas naqi africa america austrailia xray zebra spain".replace(" ", "").lower())))

#Count character occurrences
#Input: string s, character c       
#Output: number of times c appears in s
def CountCharacterOccurrences(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count
print(CountCharacterOccurrences("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up.", 'o'))
print(CountCharacterOccurrences("Python Programming is fun!", 'g')) 

#Find all indices of a character
#Input: string s, character c
#Output: list of indices where c appears in s
def FindAllIndices(s, c):
    indices = []
    for i in range(len(s)):
        if s[i] == c:
            indices.append(i)
    return indices
print(FindAllIndices("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up.", 'H'))
print(FindAllIndices("Python Programming is fun!", 'g'))

#Count words starting with a vowel
#Input: string s
#Output: number of words starting with a vowel
def CountWordsStartingWithVowel(s):
    words = s.split()
    count = 0
    for word in words:
        if word and word[0].lower() in "aeiou":
            count += 1
    return count
print(CountWordsStartingWithVowel("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(CountWordsStartingWithVowel("Python Programming is fun!"))

#Count characters in words
#Input: string s    
#Output: dictionary with word as key and character count as value
def CountCharactersInWords(s):
    words = s.split()
    char_count = {}
    for word in words:
        char_count[word] = len(word)
    return char_count   
print(CountCharactersInWords("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(CountCharactersInWords("Python Programming is fun!"))

#Find the smallest word in a string
#Input: string s
#Output: smallest word (split by spaces)
def SmallestWord(s):
    words = s.split()
    smallest = words[0] if words else ""
    for word in words:
        if len(word) < len(smallest):
            smallest = word
    return smallest
print(SmallestWord("Hello World is my first program in python! I love programming and coding. It builds the logical skills and mind opens up."))
print(SmallestWord("Python Programming is fun!"))   