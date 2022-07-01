from src.create_db_phages import create_database_phages
from src.blast_db_RBPs import run_blast, filter_homologous
from src.file_format_conversion import gb_to_faa

if __name__ == "__main__":
    create_database_phages("phages.faa", "phages")
    gb_to_faa("NC_007024.gb.txt", "NC_007024_converted.faa")
    run_blast("NC_007024_converted.faa", "phages", "results_output2.xml")
    potential_rbps = filter_homologous("results_output2.xml", 2)
    print(potential_rbps)