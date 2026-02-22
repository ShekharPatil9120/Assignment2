# ---------------------------------------------------
# Question 3: String Manipulator
# Ask the user for a sentence and display:
# 1. Original sentence
# 2. Total characters (with spaces)
# 3. Total characters (without spaces)
# 4. Total words
# 5. UPPERCASE
# 6. lowercase
# 7. Title Case
# 8. First word
# 9. Last word
# 10. Reversed sentence
# ---------------------------------------------------

try:
    # Taking input
    sentence = input("Enter a sentence: ")

    print("\n--- Output ---")

    # Original
    print("Original:", sentence)

    # Characters with spaces
    print("Characters (with spaces):", len(sentence))

    # Characters without spaces
    no_space = sentence.replace(" ", "")
    print("Characters (without spaces):", len(no_space))

    # Words
    words = sentence.split()
    print("Total words:", len(words))

    # Uppercase
    print("UPPERCASE:", sentence.upper())

    # Lowercase
    print("lowercase:", sentence.lower())

    # Title Case
    print("Title Case:", sentence.title())

    # First and Last word
    if len(words) > 0:
        print("First word:", words[0])
        print("Last word:", words[-1])
    else:
        print("No words found")

    # Reversed sentence
    print("Reversed:", sentence[::-1])

except:
    print("Something went wrong. Please try again.")