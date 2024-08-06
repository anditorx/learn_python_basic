class Employee():
    
    def __init__(self, lokasi_file):
        self.data_employee = open(f"{lokasi_file}", mode="r", encoding="utf-8")
        self.data_per_sesi = 10
        
    def baca_data(self):
        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee
    
    def hapus_data(self, baris, kolom):
        del self.data_employee[baris][kolom]
        
    def tambah_data(self, data_baru):
        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])
        
    
# Membuat object
it = Employee(lokasi_file="./karyawan_it.xls")
marketing = Employee(lokasi_file="./karyawan_marketing.xls")
product = Employee(lokasi_file="./karyawan_product.xls")