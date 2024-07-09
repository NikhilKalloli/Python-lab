def add_entry(dictionary):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    dictionary[word] = meaning
    print("Entry added successfully")

def search_word(dictionary):
    word = input("Enter the word to search: ")
    if word in dictionary:
        print(f"Meaning of {word} is {dictionary[word]}")
    else:
        print(f"{word} not found in the dictionary")

def find_words(dictionary):
    meaning = input("Enter the meaning to search: ")
    words = [word for word, m in dictionary.items() if m == meaning]
    if words:
        print(f"Words with meaning {meaning} are: {', '.join(words)}")
    else:
        print(f"No words found with meaning {meaning}")

def remove_entry(dictionary):
    word = input("Enter the word to remove: ")
    if word in dictionary:
        del dictionary[word]
        print(f"{word} removed successfully")
    else:
        print(f"{word} not found in the dictionary")

def display_words(dictionary):
    for word in sorted(dictionary):
        print(f"{word}: {dictionary[word]}")

def main():
    dictionary = {}
    while True:
        print("\n1. Add new entry")
        print("2. Search for a word")
        print("3. Find words with same meaning")
        print("4. Remove an entry")
        print("5. Display all words sorted alphabetically")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_entry(dictionary)
        elif choice == 2:
            search_word(dictionary)
        elif choice == 3:
            find_words(dictionary)
        elif choice == 4:
            remove_entry(dictionary)
        elif choice == 5:
            display_words(dictionary)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()