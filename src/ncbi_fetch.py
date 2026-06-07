from Bio import Entrez, SeqIO
Entrez.email = "diegoblancob2011@gmail.com"
genes_list = ["NM_000484.4", "NM_001377265", "KR710721.1"]

def fetch_sequence(accession_id):
    try:
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        print(f"Successfully fetched sequence for {accession_id}")
        print(f"Sequence ID: {record.id}") 
        print(f"Sequence length: {len(record.seq)}")
        return record
    except Exception as e:
        print(f"Error fetching sequence for {accession_id}: {e}")
        return None
   
    
def genes_loop():   
    for gene in genes_list:
        fetch_sequence(gene)


genes_loop()
