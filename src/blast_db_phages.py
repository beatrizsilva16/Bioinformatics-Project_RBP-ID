import subprocess
import xml.etree.ElementTree as ET


def run_blast(genome_file, database_name, results_output_file, et):
    if "faa" in genome_file:
        blast_type = "blastp"
    elif "fna" in genome_file:
        blast_type = "blastx"
    else:
        raise TypeError("Insert a genome file with correct format")

    process = subprocess.Popen(f"{blast_type} -query {genome_file} "
                               f"-out {results_output_file} -outfmt 5 "
                               f"-db {database_name} "
                               f"-evalue {et}")

    process.wait()


def filter_homologous(results_output_file):
    keywords = ["phage tail fiber protein", "tail protein", "receptor-binding tail protein",
                "short tail fibers", "tail fiber protein", "putative tail fiber protein",
                "tailspike protein", "phage tailspike protein", "receptor binding protein",
                "putative receptor-binding protein"]

    k_dict = {k: 0 for k in keywords}

    tree = ET.parse(results_output_file)
    root = tree.getroot()

    for child in root.iter():
        if child.tag == "hit-def":
            print(child.text)
            for k in keywords:
                if k in child.text.lower():
                    k_dict[k] += 1

    print(k_dict)
