import subprocess


def create_database_RBPs(db_fasta_file, database_name):
    process = subprocess.Popen(f" makeblastdb -in {db_fasta_file} -dbtype prot -out {database_name}", shell=True,
                               stdout=subprocess.PIPE)

    process.wait()
