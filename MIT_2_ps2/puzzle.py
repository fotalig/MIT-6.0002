import string


def map_dict(shift):
    alphabet = string.ascii_lowercase
    print(len(alphabet))
    mapped_dict = {}
    for i, letter in enumerate(alphabet):
        index = i + shift
        while index > 25:
            index -= 26
        mapped_dict[letter] = alphabet[index]
    return mapped_dict

test_string = """http://www.pythonchallenge.com/pc/def/map.html"""


new_string = ""
mapped_dict = map_dict(2)
for character in test_string:
    if character.lower() in mapped_dict:
        new_string += mapped_dict[character.lower()]
    else:
        new_string += character.lower()

print(new_string)