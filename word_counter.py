# program to count words in a text file
from collections import Counter

# open the text file, ask the user for the file name
file_name = input("Enter the name of the text file: ")

try:
    # read the content of the file
    with open(file_name, 'r') as file:
        text = file.read()

    # count the words
    words = text.split()
    
    # print the number of words
    print(f"The file {file_name} has {len(words)} words.")
    
    # optionally print the words (uncomment if needed)
    # print(words)
    
    # count word frequencies and display the 10 most common words
    word_count = Counter(words)
    print(f"The 10 most common words in the file {file_name} are: {word_count.most_common(10)}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")