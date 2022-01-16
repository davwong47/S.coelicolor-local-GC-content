"""Module containing utility functions for working with FASTA files."""

import re

def is_description_line(line):
    """Return True if the line is a FASTA description line."""
    if line.startswith(">"):
        return True
    return False

def test_is_description_line():
    """Test the is_description_line() function."""
    print("Testing the is_description_line() function...")
    assert is_description_line(">This is a description line") is True
    assert is_description_line("ATCG") is False

def extract_organism_name(line):
    """Return the organism name from a FASTA description line."""
    match = re.search(r"OS=(.*?) [A-Z]{2}=", line)
    return match.group(1)

def test_extract_organism_name():
    """Test the extract_organism_name() function."""
    print("Testing the extract_organism_name() function...")
    lines = [">sp|P01090|2SS2_BRANA Napin-2 OS=Brassica napus PE=2 SV=2",
        ">sp|Q15942|ZYX_HUMAN Zyxin OS=Homo sapiens GN=ZYX PE=1 SV=1",
        ">sp|Q6QGT3|A1_BPT5 A1 protein OS=Escherichia phage T5 GN=A1 PE=2 SV=1"]
    organism_names = ["Brassica napus", "Homo sapiens", "Escherichia phage T5"]
    for line, organism_name in zip(lines, organism_names):
        assert extract_organism_name(line) == organism_name, extract_organism_name(line)

if __name__=="__main__":
    test_is_description_line()
    test_extract_organism_name()