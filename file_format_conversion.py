from Bio import SeqIO
from Bio import Entrez
import os


def AN_gb(file_name):
    Entrez.email = "beatrizf.2000@gmail.com"
    nlist = [line.rstrip() for line in open(file_name)]
    for k in nlist:
        handle = Entrez.efetch(db="sequences", id=k, rettype="gb", retmode="text")

        with open(k + ".gb", "w") as file:
            file.write(handle.read())

        gb_to_faa(k + ".gb", "phages.faa")
        os.remove(k + ".gb")

def gb_to_faa(gbk_filename, faa_filename):
    input_handle = open(gbk_filename, "r")
    output_handle = open(faa_filename, "a")

    for seq_record in SeqIO.parse(input_handle, "genbank"):
        for seq_feature in seq_record.features:
            if seq_feature.type == "CDS":
                if len(seq_feature.qualifiers.get("translation", [])) >= 1:
                    output_handle.write(">%s | %s | %s | %s\n%s\n" % (
                        seq_feature.qualifiers.get('locus_tag', ["undefined"])[0],
                        seq_feature.qualifiers.get("function", ["undefined"])[0],
                        seq_feature.qualifiers.get("note", ["no notes"])[0],
                        seq_feature.qualifiers.get("product", ["no product"])[0],
                        seq_feature.qualifiers['translation'][0]))
    output_handle.close()
    input_handle.close()
