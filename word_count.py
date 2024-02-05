"""
This module provides functionality to count occurrences of each word in one or more text files.
It prints out the results and writes them into a file named 'WordCountResults.txt'.
"""

import sys
import time

def count_words(file_path):
    """
    Count the occurrence of each alphabetic word in the given file.
    
    :param file_path: string, the path to the file to be processed
    :return: dict, a dictionary mapping words to their frequency
    """
    word_count = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word.isalpha():  # checks if the word contains only letters
                        word = word.lower()  # convert to lower case
                        word_count[word] = word_count.get(word, 0) + 1
                    else:
                        print(f"Found invalid data in {file_path}: {word}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except IOError as e:
        print(f"An error occurred while processing {file_path}: {e}")
    
    return word_count

def main():
    """
    Main function to read multiple files provided as command-line arguments and count the words.
    """
    if len(sys.argv) < 2:
        print("Usage: python word_count.py file_with_data1.txt [file_with_data2.txt ...]")
        sys.exit(1)

    start_time = time.time()

    with open('word_count_results.txt', 'w', encoding='utf-8') as results_file:
        for file_path in sys.argv[1:]:
            word_count = count_words(file_path)
            results_file.write(f"Results for {file_path}:\n")
            for word, count in sorted(word_count.items()):
                results_file.write(f"{word}: {count}\n")
            results_file.write("\n")

    elapsed_time = time.time() - start_time
    print(f"Word count for all files has been completed.")
    print(f"Time elapsed for all files: {elapsed_time:.2f} seconds")
    with open('word_count_results.txt', 'a', encoding='utf-8') as results_file:
        results_file.write(f"Total time elapsed for all files: {elapsed_time:.2f} seconds\n")

if __name__ == "__main__":
    main()
