from Bio import SeqIO


def gb_to_faa(gbk_filename, faa_filename):

    input_handle = open(gbk_filename, "r")
    output_handle = open(faa_filename, "w+")

    for seq_record in SeqIO.parse(input_handle, "genbank"):
        for seq_feature in seq_record.features:
            if seq_feature.type == "CDS":
                assert len(seq_feature.qualifiers['translation']) == 1
                output_handle.write(">%s | %s | %s | %s\n%s\n" % (
                    seq_feature.qualifiers['locus_tag'][0],
                    seq_feature.qualifiers.get("function", ["undefined"])[0],
                    seq_feature.qualifiers.get("note", ["no notes"])[0],
                    seq_feature.qualifiers.get("product", ["no product"])[0],
                    seq_feature.qualifiers['translation'][0]))
    output_handle.close()
    input_handle.close()
