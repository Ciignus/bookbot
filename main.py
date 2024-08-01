from collections import Counter
import string
def count_words(text):

    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    
    filtered_text = ''.join(char for char in text if char in string.ascii_lowercase)
    
    char_count = Counter(filtered_text)
    
    return dict(char_count)


def print_report(text):
    word_count = count_words(text)
    char_count = count_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_count:
        if char.isprintable() and not char.isspace():
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("File contents:")
    print(file_contents)
    print()

    print_report(file_contents)

if __name__ == "__main__":
    main()
