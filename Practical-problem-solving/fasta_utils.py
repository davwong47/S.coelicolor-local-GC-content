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

def organism_name2species(organism_name):
    """Return the species from the FASTA organism name."""
    words = organism_name.split()
    return words[0] + " " + words[1]

def test_organism_name2species():
    print("Testing the organism_name2species() function...")
    assert organism_name2species("Methylomonas sp. (strain J)") == "Methylomonas sp."
    assert organism_name2species("Homo sapiens") == "Homo sapiens"

def summarise_species_protein_data(fasta_desc_lines):
    """Return data structure summarising the organism and protein data"""
    summary = dict()
    for line in fasta_desc_lines:
        variant_name = extract_organism_name(line)
        species_name = organism_name2species(variant_name)
        variant_dict = summary.get(species_name, dict())
        variant_dict[variant_name] = variant_dict.get(variant_name, 0) + 1
        summary[species_name] = variant_dict
    return summary

def test_summarise_species_protein_data():
    print("Testing summarise_species_protein_data() function...")
    fasta_desc_lines = [
">sp|P12334|AZUR1_METJ Azurin iso-1 OS=Methylomonas sp. (strain J) PE=1 SV=2",
">sp|P12335|AZUR2_METJ Azurin iso-2 OS=Methylomonas sp. (strain J) PE=1 SV=1",
">sp|P23827|ECOT_ECOLI Ecotin OS=Escherichia coli (strain K12) GN=eco PE=1 SV=1",
">sp|B6I1A7|ECOT_ECOSE Ecotin OS=Escherichia coli (strain SE11) GN=eco PE=3 SV=1"
    ]
    summary = summarise_species_protein_data(fasta_desc_lines)

    # The top level dictionary will contain two entries.
    assert len(summary) ==2
    assert "Methylomonas sp." in summary
    assert "Escherichia coli" in summary

    # The value of the Methylomonas sp. entry is a dictionary with one
    # entry in it.
    assert len(summary["Methylomonas sp."]) == 1
    assert summary["Methylomonas sp."]["Methylomonas sp. (strain J)"] == 2

    # The value of the Escherichia coli entry is a dictionary with two
    # entries in it.
    assert len(summary["Escherichia coli"]) == 2
    assert summary["Escherichia coli"]["Escherichia coli (strain K12)"] == 1
    assert summary["Escherichia coli"]["Escherichia coli (strain SE11)"] == 1

if __name__=="__main__":
    test_is_description_line()
    test_extract_organism_name()
    test_organism_name2species()
    test_summarise_species_protein_data()