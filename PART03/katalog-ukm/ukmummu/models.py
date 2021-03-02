from ukmummu import db


class Tindustri(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    industri = db.Column(db.String(15), unique=True, nullable=False)
    ket = db.Column(db.String(100), nullable=True)
    ukms = db.relationship('Tukm', backref='ukms',lazy=True)
    
    def __repr__(self):
        return f"Tindustri('{self.industri}','{self.ket}')"

class Tukm(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nama_ukm = db.Column(db.String(100), nullable=False)
    industri_id = db.Column (db.Integer, db.ForeignKey('tindustri.id'))
    no_izin= db.Column(db.String(60), nullable=False, unique=True)
    thn_berdiri= db.Column(db.String(60), nullable=True)
    alamat= db.Column(db.String(60), nullable=True)
    propinsi= db.Column(db.String(60), nullable=True)
    kota= db.Column(db.String(60), nullable=True)
    kecamatan= db.Column(db.String(60), nullable=True)
    nama_pemilik= db.Column(db.String(100), nullable=True)
    no_ktp= db.Column(db.String(20), nullable=True)
    no_hp= db.Column(db.String(25), nullable=True)
    username= db.Column(db.String(60), nullable=True)
    password= db.Column(db.String(60), nullable=True)
    gambar = db.Column(db.String(60), nullable=False, default='gambarfoto.jpg')
    uproduks = db.relationship('Tproduk', backref='ukmproduk',lazy=True)
    def __repr__(self):
        return f"Tukm('{self.nama_ukm}','{self.industri_id}','{self.no_izin}','{self.thn_berdiri}', '{self.alamat}','{self.propinsi}', '{self.kota}', '{self.kecamatan}', '{self.nama_pemilik}', '{self.no_ktp}', '{self.username}', '{self.password}', '{self.gambar}')"


class Tkategori(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    kategori = db.Column(db.String(50), unique=True, nullable=False)
    ket = db.Column(db.String(250), nullable=True)
    kproduks = db.relationship('Tproduk', backref='kategoriproduk',lazy=True)
    
    def __repr__(self):
        return f"Tkategori('{self.kategori}','{self.ket}')"


class Tproduk(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    no_pirt = db.Column(db.String(100), nullable=False)
    no_lppom = db.Column(db.String(100), nullable=True)
    nama_produk = db.Column(db.String(100), nullable=False)
    kategori_id = db.Column (db.Integer, db.ForeignKey('tkategori.id'))
    harga= db.Column(db.String(100), nullable=False)
    deskripsi= db.Column(db.String(60), nullable=False)
    stok= db.Column(db.String(60), nullable=False)
    gambar = db.Column(db.String(30), nullable=False, default='gambarproduk.jpg')
    ukm_id = db.Column (db.Integer, db.ForeignKey('tukm.id'))
    def __repr__(self):
        return f"Tproduk('{self.no_pirt}','{self.no_lppom}','{self.nama_produk}','{self.kategori_id}', '{self.harga}','{self.deskripsi}', '{self.stok}', '{self.gambar}', '{self.gambar}')"


class Tadmin(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"Tadmin('{self.username}','{self.password}')"
        