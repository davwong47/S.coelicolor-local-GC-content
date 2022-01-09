def parse_dna(file_handle):
    """Return DNA sequence as a list."""
    first_line = next(file_handle) #discard first line
    sequence = []
    for line in file_handle:
        words = line.split() 
        seq_string = "".join(words[:-1]) 
        seq_list = list(seq_string)
        sequence.extend(seq_list) 
    return sequence

def gc_content(sequence):
    """Return GC-content as a percentage from a list of DNA letters."""
    gc_count = sequence.count('g') + sequence.count('c')
    gc_fraction = float(gc_count) / len(sequence)
    return 100 * gc_fraction

def sliding_window_analysis(sequence, function, 
                            window_size=100000, step_size=50000):
    """Return an iterator that yields (start, end, property) tuples.
    
    Where start and end are the indices used to slice the input list and 
    property is the return value of the function given the sliced list.
    """
    for start in range(0, len(sequence), step_size):
        end = start + window_size
        if end > len(sequence):
            break
        yield start, end, function(sequence[start:end])

with open("Sco.dna", "r") as file_handle:
    sequence = parse_dna(file_handle)

with open("local_gc_content.csv", "w") as file_handle:
    header = "start,middle,end,gc_content\n"
    file_handle.write(header)
    for start, end, gc in sliding_window_analysis(sequence, gc_content):
        middle = (start + end) / 2
        row = "{},{},{},{}\n".format(start, middle, end, gc)
        file_handle.write(row)