from src.blast_db_RBPs import run_blast
from src.create_db_RBPs import create_database_RBPs
from src.file_format_conversion import gb_to_faa
from blast_db_phages import filter_homologous

if __name__ == "__main__":
    gb_to_faa("NC_002730.gb.txt", "NC_002730_converted.faa")
    create_database_RBPs("database_rbps.faa", "rbps")
    run_blast("NC_002730_converted.faa", "rbps", "results_RBPs.xml", 1e-20)
    run_blast("NC_002730_converted.faa", "rbps", "results_phages.xml", 1e-20)
    filter_homologous("results_phages.xml")
