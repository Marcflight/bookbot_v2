import sys
from stats import get_num_of_words, get_num_of_chars, sort_num_of_chars

def main():
    filepath = extract_file(sys.argv)                                   #define File
    text = get_book_text(filepath)                          #extract file as a str
    num_words = get_num_of_words(text)                      #count words in file str
    num_of_chars = get_num_of_chars(text)                   #count characters in file str
    sorted_chars = sort_num_of_chars(num_of_chars)
    print_report(filepath, num_words, sorted_chars)

def get_book_text(path):                                    #open file and extract text as str
    with open(path) as f:
        return f.read()
    
def extract_file(path):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]
    
def print_report(filepath, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()