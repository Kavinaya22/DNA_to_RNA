from rosalind import getFasta, gcContent

fasta = getFasta("rosalind_gc.text")

for label in fasta:
    print(gcContent(fasta[label]))
    
