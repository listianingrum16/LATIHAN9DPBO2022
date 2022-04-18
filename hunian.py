class Hunian():
    def __init__(self, jenis, jml_penghuni = 0, jml_kamar = 0, luas_tanah = 0, kps_listrik = 0, harga_sewa = 0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah
        self.kps_listrik = kps_listrik
        self.harga_sewa = harga_sewa

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_luas_tanah(self):
        return self.luas_tanah

    def get_kps_listrik(self):
        return self.kps_listrik
    
    def get_harga_sewa(self):
        return self.harga_sewa

    def get_dokumen(self):
        pass