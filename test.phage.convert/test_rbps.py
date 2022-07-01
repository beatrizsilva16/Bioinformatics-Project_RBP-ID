from src.create_db_RBPs import create_database_RBPs
from src.blast_db_RBPs import run_blast, filter_homologous
from file_format_conversion import gb_to_faa

if __name__ == "__main__":
    create_database_RBPs("database_rbps.txt", "rbps")
    gb_to_faa("NC_002730.gb.txt", "NC_002730_converted.faa")
    run_blast("NC_002730._converted.faa","rbps", "results_output1.xml")
    potential_rbps = filter_homologous("results_output1.xml", 2)
    print(potential_rbps)
