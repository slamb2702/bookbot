
def count_words(file_contents):
    file_words = []
    file_words = file_contents.split()

    return(len(file_words))


def count_characters_dict(text):

    chars = {}

    for c in text:
        lowercase = c.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1

    return chars



def sort_on(x):
    return x["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

