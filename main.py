def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_of_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_of_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

    
main()