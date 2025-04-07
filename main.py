
def get_book_text(path_to_file):
    with open(path_to_file) as f:
    
        file_contents = f.read()

        return file_contents

def main():

    from stats import count_words, count_characters


    relative_path = "books/frankenstein.txt"

    file_contents = get_book_text(relative_path)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print(f"{word_count} words found in the document")
    print(char_count)

if __name__ == "__main__":
    main()