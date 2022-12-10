import os
from data_utils import get_unique_model_nums, get_unique_serial_nums, get_sorted_model_num_freqs, get_sorted_serial_num_freqs, get_sorted_model_num_chars, get_sorted_serial_num_chars, get_sorted_model_num_char_freqs, get_sorted_serial_num_char_freqs

# Write every unique model number to file.
def compile_model_nums():
    with open("model_num_stats/model_nums.txt", "w") as f:
        for model_num in get_unique_model_nums():
            f.write(model_num + "\n")

# Write every unique serial number to file.
def compile_serial_nums():
    with open("serial_num_stats/serial_nums.txt", "w") as f:
        for serial_num in get_unique_serial_nums():
            f.write(serial_num + "\n")

# Write the frequency of every model # to file; format -> model number : frequency.
def compile_model_num_freq():
    freqs = get_sorted_model_num_freqs()
    with open("model_num_stats/model_num_freqs.txt", "w", encoding="utf-8") as f:
        for key in freqs:
            f.write(key + " : " + str(freqs[key]) + "\n")

# Write the frequency of every serial # to file; format -> serial number : frequency.
def compile_serial_num_freq():
    freqs = get_sorted_serial_num_freqs()
    with open("serial_num_stats/serial_num_freqs.txt", "w", encoding="utf-8") as f:
        for key in freqs:
            f.write(key + " : " + str(freqs[key]) + "\n")
    
# Write all characters present in model numbers to file.
def compile_model_num_chars():
    with open("model_num_stats/model_num_chars.txt", "w", encoding="utf-8") as f:
        for char in get_sorted_model_num_chars():
            f.write(char)

# Write all characters present in serial numbers to file.
def compile_serial_num_chars():
    with open("serial_num_stats/serial_num_chars.txt", "w", encoding="utf-8") as f:
        for char in get_sorted_serial_num_chars():
            f.write(char)

# Write the frequency of every model number character to file; format -> character : frequency.
def compile_model_num_chars_freq():
    freqs = get_sorted_model_num_char_freqs()
    with open("model_num_stats/model_num_chars_freq.txt", "w", encoding="utf-8") as f:
        for key in freqs:
            f.write(key + " : " + str(freqs[key]) + "\n")

# Write the frequency of every serial number character to file; format -> character : frequency.
def compile_serial_num_chars_freq():
    freqs = get_sorted_serial_num_char_freqs()
    with open("serial_num_stats/serial_num_chars_freq.txt", "w", encoding="utf-8") as f:
        for key in freqs:
            f.write(key + " : " + str(freqs[key]) + "\n")

# Entry function.
def main():
    if not os.path.exists("model_num_stats"):
        os.makedirs("model_num_stats")
        compile_model_nums()
        compile_model_num_freq()
        compile_model_num_chars()
        compile_model_num_chars_freq()
    
    if not os.path.exists("serial_num_stats"):
        os.makedirs("serial_num_stats")
        compile_serial_nums()
        compile_serial_num_freq()
        compile_serial_num_chars()
        compile_serial_num_chars_freq()

main()

