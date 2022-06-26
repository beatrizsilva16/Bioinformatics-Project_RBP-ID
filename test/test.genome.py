from src.blast import run_blast
from src.create_db import create_rbps_database

if __name__ == "__main__":
    create_rbps_database("database_rbps.faa", "rbps")
    run_blast("sequencia_teste.faa", "rbps", "results.xml",1e-20)
