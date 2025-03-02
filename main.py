from stats import get_num_of_words, get_num_of_chars

def main():
    filepath = "books/frankenstein.txt"                     #define File
    text = get_book_text(filepath)                          #extract file as a str
    num_words = get_num_of_words(text)                      #count words in file str
    num_of_char = get_num_of_chars(text)                    #count characters in file str 
    print(f"{num_words} words found in the document")
    print(num_of_char)

def get_book_text(path):                                    #open file and extract text as str
    with open(path) as f:
        return f.read()
    
main()