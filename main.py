def main():
    book_path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    word_count = get_word_count(file_contents)
    chars_dict = get_chars(file_contents)
    chars_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(file_contents)} words found in the document")
    print()

    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_word_count(book):
    words = book.split()
    return len(words)

def sort_on(d):
    return d["num"]

def get_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    main()