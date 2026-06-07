from Bio.Seq import Seq

def compare_sequences(seq1, seq2):
    """Compare two sequences and return similarity percentage"""
    min_len = min_len = min(len(seq1), len(seq2))
    seq1_trim = seq1[:min_len]
    seq2_trim = seq2[:min_len]
    matches = sum(a == b for a, b in zip(seq1_trim, seq2_trim))
    return (matches / min_len) * 100
