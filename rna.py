#The code down below converts a DNA string to an RNA string by changing "T with U"
#rosalind_dna.txt is the DNA string
dna = open("rosalind_rna.txt", "r").read()
new_rnastring = dna.replace("T", "U", 1000)
print(new_rnastring)
