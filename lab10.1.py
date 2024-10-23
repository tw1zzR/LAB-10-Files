import sys

# Opening file
x = "story.txt"
with open(x, "r", encoding="utf-8") as file:
    content = file.read()

print(f"\nText from file: {content}")

# Convert words to lower register
lower_content = content.lower()

# Words list
words = lower_content.split()
print(f"\nAll words in file: {words}")

# Words count
words_count = len(words)
print(f"Words count: {words_count}")

# Unique words
unique_w = set(words)
words_unique = len(unique_w)
print(f"Unique words: {words_unique}")

# Sentence count
sentence_count = content.count(".")
print(f"Sentence count: {sentence_count}")

# Result to file
with open("words.txt", "w") as file:
    sys.stdout = file
    print(f"Text from file: {content}")
    print(f"\nAll words in file: {words}")
    print(f"Words count: {words_count}")
    print(f"Unique words: {words_unique}")
    print(f"Sentence count: {sentence_count}")
    sys.stdout = sys.__stdout__
print("\nResults of analysis are recorded in words.txt")
