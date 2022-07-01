import subprocess
from Bio.SearchIO.BlastIO import BlastXmlParser


def run_blast(genome_file, database_name, results_output_file):
    if "faa" in genome_file:
        blast_type = "blastp"
    elif "fna" in genome_file:
        blast_type = "blastx"
    else:
        raise TypeError("Insert a genome file with correct format")

    process = subprocess.Popen(f"{blast_type} -query {genome_file} "
                               f"-out {results_output_file} -outfmt 5 "
                               f"-db {database_name} "
                               )

    process.wait()


def filter_homologous(results_output_file, e_value_threshold):

    blast_file = open(results_output_file)
    handle = BlastXmlParser(blast_file)
    potential_rbps_homologous = []
    potential_rbps_homologous_and_keywords = []
    for blast_record in handle:
        description = blast_record.description
        if len(blast_record.hits) > 0:
            hits = blast_record.hits
            hsps = blast_record.hsps
            for i in range(len(hits)):
                hsp = hsps[i]
                if hsp.evalue < e_value_threshold:
                    found = check_keyword_in_description(description)
                    if blast_record.id not in potential_rbps_homologous:
                        potential_rbps_homologous.append(blast_record.id)
                        if found:
                            potential_rbps_homologous_and_keywords.append(blast_record.id)

    blast_file.close()
    return potential_rbps_homologous, potential_rbps_homologous_and_keywords


def check_keyword_in_description(description):
    keywords = ["phage tail fiber protein", "tail protein", "receptor-binding tail protein",
                "short tail fibers", "tail fiber protein", "putative tail fiber protein",
                "tailspike protein", "phage tailspike protein", "receptor binding protein",
                "putative receptor-binding protein", "tail spike protein", "tailfiber", "minor tail protein",
                "putative minor tail protein"]

    found = False
    for k in keywords:
        if k in description.lower():
            found = True

    return found
