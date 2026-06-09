from Bio import Entrez, SeqIO
Entrez.email = "diegoblancob2011@gmail.com"
genes_list = ["NM_000484.4", "NM_001377265", "KR710721.1"]


def fetch_sequence(accession_id):
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        gen={
        "Sequence ID": record.id,
        "Sequence length": len(record.seq),
        "gc": (record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100,
        "sequence": record.seq
        }
        return gen
    except Exception as e:
        print(f"Error fetching sequence for {accession_id}: {e}")
        return None
   
    
def genes_loop():
    for gene in genes_list:
        result = fetch_sequence(gene)
        print(result)

genes_loop()