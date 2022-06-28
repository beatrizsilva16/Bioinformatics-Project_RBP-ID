from src.create_db_phages import create_database_phages
from src.blast_db_phages import filter_homologous

if __name__ == "__main__":
    create_database_phages("phage_genomes.txt", "phages")
    filter_homologous("results_phages.xml")
