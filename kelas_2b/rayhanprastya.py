import pandas as pd
import csv

class rayprastya(object):
    def convert(self):
        read_file = pd.read_csv (r'kelas_2b/raypras.csv')
        read_file.to_excel (r'kelas_2b/raypras.xlsx', index = None, header=True)
        print("file berhasil dirubah")