

from stats import (
    count_words,
    chars_dict_to_sorted_list,
    count_characters_dict,
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    
        file_contents = f.read()

        return file_contents

def main():

    import sys


    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_characters_dict(file_contents)
    char_count_sorted = chars_dict_to_sorted_list(char_count)

    print_report(book_path, word_count, char_count_sorted)



def print_report(book_path, word_count, char_count_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_count_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()

