
def count_words(file_contents):
    file_words = []
    file_words = file_contents.split()



    return(len(file_words))


def count_characters(text):

    chars = {}
    
    for c in text:
        lowercase = c.lower

        if lowercase in chars:
            chars[lowercase] += 1
        
        else
            chars[lowercase] = 1

    return chars

