import csv
from data_utils import get_sorted_model_num_freqs, get_sorted_serial_num_freqs, get_most_freq_model_num_char, get_most_freq_serial_num_char, get_max_number_length, get_ASCII_min, get_ASCII_max

# Create new csv file in preparation for manual cleaning -> 1) Sequence (model/serial #); 2) Label (is this a model or serial number?); 3) Scaled ASCII value of each string character (each character's ASCII value will be put in its own column).
def reformat_dirty():
    model_freqs = get_sorted_model_num_freqs()
    serial_freqs = get_sorted_serial_num_freqs()

    min = get_ASCII_min()
    max = get_ASCII_max()
    print(min)
    print(max)
    max_bound = max - min                                                                # Move range down to 0 (e.g. 30 - 60 -> 0 - 30).
    model_filler = (ord(get_most_freq_model_num_char()) - min) / max_bound
    serial_filler = (ord(get_most_freq_serial_num_char()) - min) / max_bound
    max_num_len = get_max_number_length()

    header = ['sequence', 'label']
    for x in range(max_num_len):
        header.append("P" + str(x))

    with open("datasets/dirty2.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for key in model_freqs:
            val = model_freqs[key]
            if val < 2:
                break
            # The label will be 0 for model numbers, fill missing cells with most frequently occuring model number character.
            row = [key] + ["0"] + [(ord(c) - min) / max_bound for c in key]
            while len(row) < max_num_len:
                row.append(model_filler)
            writer.writerow(row)
    
        for key in serial_freqs:
            val = serial_freqs[key]
            if val < 2:
                break
            # The label will be 1 for serial numbers, fill missing cells with the most frequently occuring serial number character.
            row = [key] + ["1"] + [(ord(c) - min) / max_bound for c in key]
            while len(row) < max_num_len:
                row.append(serial_filler)
            writer.writerow(row)
    
def main():
    reformat_dirty()
    
main()