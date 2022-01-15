"""Module containing utility functions for working with FASTA files."""

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

test_is_description_line()