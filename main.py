
def main():
    with open("books/frakenstein.txt") as f:
        file_contents  = f.read()
        print(f"Number of words in text document: {get_number_of_words(file_contents)}")

def get_number_of_words(file_text):
    count_text = file_text.split()
    return len(count_text)

if __name__ == "__main__":
    main()