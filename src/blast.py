import subprocess

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

def filter_homologous (results_file):
    pass

