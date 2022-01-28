#Developed by A NAVEEN KUMAR
#Reference no :21004621
# To write a program for getting the word count from a file.
num_of_words = 0
file = open('wordtext.txt')
wordtext = file.read()
words = wordtext.split()
num_of_words = len(words)
print("Number of words = ",num_of_words)