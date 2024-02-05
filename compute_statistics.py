"""
This module computes basic statistical measures such as mean, median, mode,
standard deviation, and variance for a set of numbers provided in a text file.
It handles multiple files and writes the computed statistics to an output file.
"""

import time
import glob

def read_numbers(file_path_to_read):
    """Read numbers from a file and handle invalid entries."""
    numbers = []
    with open(file_path_to_read, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError as e:
                print(f"Error reading line: {line.strip()}, Error: {e}")
    return numbers

def calculate_mean(numbers):
    """Calculate the mean of the numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    """Calculate the median of the numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_numbers[midpoint]
    else:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2

def calculate_mode(numbers):
    """Calculate the mode of the numbers."""
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    most_frequent = max(frequency.values())
    mode = [number for number, freq in frequency.items() if freq == most_frequent]
    if len(mode) == len(set(numbers)):
        return []  # No mode if all numbers occur equally
    return mode

def calculate_variance(numbers, mean):
    """Calculate the variance of the numbers."""
    return sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)

def calculate_std_dev(variance):
    """Calculate the standard deviation of the numbers."""
    return variance ** 0.5

def process_file(file_path_to_process):
    """Process a file to calculate statistics and return the results."""
    start_time = time.time()

    numbers = read_numbers(file_path_to_process)
    if not numbers:
        return f"File {file_path_to_process} contains no valid numbers."

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_std_dev(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = (
        f"File: {file_path_to_process}\n"
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Variance: {variance}\n"
        f"Time Elapsed: {elapsed_time} seconds\n\n"
    )

    return results

# Main code to process multiple files
if __name__ == "__main__":
    file_paths = glob.glob('TC*.txt')
    all_results = ""

    for file_path in file_paths:
        results = process_file(file_path)
        all_results += results

        with open('statistics_results.txt', 'a', encoding='utf-8') as doc:
            doc.write(results)

        print(results)
