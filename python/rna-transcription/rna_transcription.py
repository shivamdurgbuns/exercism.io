def to_rna(dna_strand):
    if dna_strand=="":
        return ""
    else:
        i, j = "GCTA", "CGAU"
        t= str.maketrans(i,j)
        return dna_strand.translate(t)