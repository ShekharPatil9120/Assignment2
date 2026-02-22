# ---------------------------------------------------
# Question 19: Text Analysis
# ---------------------------------------------------

text = input("Enter text: ")
words = text.split()

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

word_freq = {}
for word in words:
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWords:", len(words))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Reversed:", text[::-1])
print("Without vowels:", "".join([c for c in text if c not in vowels]))
print("Longest word:", max(words, key=len) if words else "")
print("Word Frequency:", word_freq)