''' Write a program that takes two 5-letter words as input and finds the sum of the distance
between the respective characters of these words.
Example:
Input:
abcde
abdfe
Distance: 0-0-1-2-0
Output: 3
Input:
pqxzy
qpyax
Distance: 1-1-1-25-1
Output: 29 '''
word1 = input("Enter the first 5-letter word: ")
word2 = input("Enter the second 5-letter word: ")
if len(word1) == 5 and len(word2) == 5:
    distance = 0
    for i in range(len(word1)):
        distance += abs(ord(word1[i]) - ord(word2[i]))
    print(f"Distance: {distance}")
else:
    print("Please enter valid 5-letter words.")
    
    
    
''' without loop '''
word1 = input("Enter the first 5-letter word: ")
word2 = input("Enter the second 5-letter word: ")
if len(word1) == 5 and len(word2) == 5:
    distance1 = abs(ord(word1[0]) - ord(word2[0]))
    distance2 = abs(ord(word1[1]) - ord(word2[1]))
    distance3 = abs(ord(word1[2]) - ord(word2[2]))
    distance4 = abs(ord(word1[3]) - ord(word2[3]))
    distance5 = abs(ord(word1[4]) - ord(word2[4]))
    print(f"Distance: {distance1}-{distance2}-{distance3}-{distance4}-{distance5}")
    print(f"Output: {distance1 + distance2 + distance3 + distance4 + distance5}")
else:
    print("Please enter valid 5-letter words.")