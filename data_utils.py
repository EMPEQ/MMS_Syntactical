import pandas as pd
from collections import defaultdict

df = pd.read_csv("datasets/dirty1.csv")

# Returns list of model nums without NaN or None.
def get_model_nums():
    return list(filter(lambda num: isinstance(num, str), df["model"].tolist()))

# Returns list of serial nums without NaN or None.
def get_serial_nums():
    return list(filter(lambda num: isinstance(num, str), df["serial_number"].tolist()))

# Returns set of model nums (no duplicates).
def get_unique_model_nums():
    return set(get_model_nums())

# Return set of serial nums (no duplicates).
def get_unique_serial_nums():
    return set(get_serial_nums())

# Get dictionary where key = model number, value = # of appearances, in descending order of appearances.
def get_sorted_model_num_freqs():
    model_num_freqs = defaultdict(lambda: 0)
    for model_num in get_model_nums():
        model_num_freqs[model_num] += 1
    return dict(sorted(model_num_freqs.items(), key= lambda item: item[1], reverse=True))

# Get dictionary where key = serial number, value = # of appearances, in descending order of appearances.
def get_sorted_serial_num_freqs():
    serial_num_freqs = defaultdict(lambda: 0) 
    for serial_num in get_serial_nums():
        serial_num_freqs[serial_num] += 1
    return dict(sorted(serial_num_freqs.items(), key= lambda item: item[1], reverse=True))

# Get list of unique possible characters in model numbers, sorted by ASCII value.
def get_sorted_model_num_chars():
    model_num_chars = set()
    for model_num in get_unique_model_nums():
        for char in model_num:
            model_num_chars.add(char)
    return sorted(list(model_num_chars))

# Get list of unique possible characters in serial numbers, sorted by ASCII value.
def get_sorted_serial_num_chars():
    serial_num_chars = set()
    for serial_num in get_unique_serial_nums():
        for char in serial_num:
            serial_num_chars.add(char)
    return sorted(list(serial_num_chars))

# Get dictionary where key = model number character, value = # of appearances, in descending order of appearances.
def get_sorted_model_num_char_freqs():
    model_num_char_freqs = defaultdict(lambda: 0)
    for model_num in get_model_nums():
        for char in model_num:
            model_num_char_freqs[char] += 1
    return dict(sorted(model_num_char_freqs.items(), key= lambda item: item[1], reverse=True))

# Get dictionary where key = serial number character, value = # of appearances, in descending order of appearances.
def get_sorted_serial_num_char_freqs():
    serial_num_char_freqs = defaultdict(lambda: 0)
    for serial_num in get_serial_nums():
        for char in serial_num:
            serial_num_char_freqs[char] += 1
    return dict(sorted(serial_num_char_freqs.items(), key= lambda item: item[1], reverse=True))

# Get max number length (model and serial) in the dataset.
def get_max_number_length():
    max_model_len = len(max(list(get_unique_model_nums()), key=len))
    max_serial_len = len(max(list(get_unique_serial_nums()), key=len))
    return max(max_model_len, max_serial_len)

# Get most frequently appearing character in model numbers.
def get_most_freq_model_num_char():
    for key in get_sorted_model_num_char_freqs():
        return key

# Get most frequently appearing character in serial numbers.
def get_most_freq_serial_num_char():
    for key in get_sorted_serial_num_char_freqs():
        return key

# Get ASCII value of smallest character for model and serial numbers.
def get_ASCII_min():
    model_min = ord(get_sorted_model_num_chars()[0])
    serial_min = ord(get_sorted_serial_num_chars()[0])
    return min(model_min, serial_min)

# Get ASCII value of largest character for model and serial numbers.
def get_ASCII_max():
    model_chars = get_sorted_model_num_chars()
    serial_chars = get_sorted_serial_num_chars()
    model_max = ord(model_chars[len(model_chars) - 1])
    serial_max = ord(serial_chars[len(serial_chars) - 1])
    return max(model_max, serial_max)
