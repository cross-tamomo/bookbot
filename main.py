def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, num_words, chars_sorted_list)


def print_report(book_path, num_words, chars_sorted_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    return len(text.split())


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = [{"char": ch, "num": count} for ch, count in num_chars_dict.items()]
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
