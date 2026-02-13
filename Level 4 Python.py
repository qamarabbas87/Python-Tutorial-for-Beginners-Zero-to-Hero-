#Level 4: Dictionaries (frequency)
#Word counter
#Input: sentence
#Output: dict of word → count
def WordCounter(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count   
print(WordCounter("Hello World is my first program in python! We love programming and coding. It builds the logical skills and mind opens up."))
print(WordCounter("Python Programming is fun!"))


#Most frequent character
#Input: string
#Output: char with highest frequency
def MostFrequentCharacter(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    most_frequent = max(char_count, key=char_count.get)
    return most_frequent
print('Most frequent character : ' + MostFrequentCharacter("Python Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! gggggggggggggggggPython Programming is fun! ggggggggggggggggg"))
#print(MostFrequentCharacter("Python Programming is fun! ggggggggggggggggg"))

