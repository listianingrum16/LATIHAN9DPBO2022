from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, kps_listrik, harga_sewa):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas_tanah, kps_listrik, harga_sewa)
        self.nama_pemilik = nama_pemilik
    
    def get_summary(self):
        return "Hunian Apartemen"

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik