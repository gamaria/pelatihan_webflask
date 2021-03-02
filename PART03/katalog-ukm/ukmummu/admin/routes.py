from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request
from ukmummu import app,db,bcrypt
from ukmummu.models import Tindustri, Tukm, Tkategori, Tproduk, Tadmin
from ukmummu.admin.forms import industri_F, ukm_F, kategori_F, eindustri_F, eukm_F, ekategori_F, eadmin_F

gadmin= Blueprint('gadmin',__name__)

@gadmin.route("/tes")
def tes():
    return "Selamat datang di pelatihan"

@gadmin.route("/dasboard")
def dasboard():
    industri=len(Tindustri.query.all())
    ukm=len(Tukm.query.all())
    produk=len(Tproduk.query.all())
    return render_template("t_admin/dasboard.html", industri=industri, ukm=ukm, produk=produk)

#CRUD DATA INDUSTRI
@gadmin.route("/industri", methods=['GET', 'POST'])
def industri():
    form=industri_F()
    data=Tindustri.query.all()
    if form.validate_on_submit():
        add= Tindustri(industri=form.industri.data, ket=form.ket.data)
        db.session.add(add)
        db.session.commit()
        flash('Data berhasil ditambahkan','warning')
        return redirect(url_for('gadmin.industri'))
    return render_template("t_admin/industri.html", dataidustri=data, form=form)


@gadmin.route("/hapusindustri/<id>", methods=['GET', 'POST'])
def hapus_industri(id):
    qindustri=Tindustri.query.get(id)
    db.session.delete(qindustri)
    db.session.commit()
    flash('Data Berhasil Di hapus','warning')
    return redirect(url_for('gadmin.industri')) 

@gadmin.route("/editindustri/<int:ed_id>/update", methods=['GET', 'POST'])
def update_industri(ed_id):
    dataindustri=Tindustri.query.get_or_404(ed_id)
    form=eindustri_F()
    if form.validate_on_submit():
        dataindustri.industri=form.industri.data
        dataindustri.ket=form.ket.data
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('gadmin.industri'))
    elif request.method=="GET":
        form.industri.data=dataindustri.industri
        form.ket.data=dataindustri.ket
    return render_template('t_admin/eindustri.html', form=form)
#BATAS CRUD INDUSTRI

#CRUD ANGGOTA UKM
@gadmin.route("/anggota", methods=['GET', 'POST'])
def anggota():
    form=ukm_F()
    data=Tukm.query.all()
    form.industriid.choices = [(str(tindustri.id), tindustri.industri) for tindustri in Tindustri.query.all()]
    if form.validate_on_submit():
        pass_hash= bcrypt.generate_password_hash(form.noizin.data). decode('utf-8')
        add= Tukm(nama_ukm=form.namaukm.data, no_izin=form.noizin.data, industri_id=form.industriid.data, nama_pemilik=form.namapemilik.data, no_ktp=form.noktp.data, username=form.namaukm.data, password=pass_hash )
        db.session.add(add)
        db.session.commit()
        flash('Data berhasil ditambahkan, username:nama ukm dan password:no izin','warning')
        return redirect(url_for('gadmin.anggota'))
    return render_template("t_admin/anggota.html", dataukm=data,form=form )


@gadmin.route("/hapusukm/<id>", methods=['GET', 'POST'])
def hapus_ukm(id):
    qukm=Tukm.query.get(id)
    db.session.delete(qukm)
    db.session.commit()
    flash('Data Berhasil Di hapus','warning')
    return redirect(url_for('gadmin.anggota')) 


@gadmin.route("/editukm/<int:ed_id>/update", methods=['GET', 'POST'])
def update_ukm(ed_id):
    dataukm=Tukm.query.get_or_404(ed_id)
    form=eukm_F()
    form.industriid.choices = [(str(tindustri.id), tindustri.industri) for tindustri in Tindustri.query.all()]
    if form.validate_on_submit():
        pass_hash= bcrypt.generate_password_hash(form.noizin.data). decode('utf-8')
        dataukm.nama_ukm=form.namaukm.data
        dataukm.no_izin=form.noizin.data
        dataukm.industri_id=form.industriid.data
        dataukm.nama_pemilik=form.namapemilik.data
        dataukm.no_ktp=form.noktp.data
        dataukm.username=form.namaukm.data
        dataukm.password=pass_hash
        db.session.commit()
        flash('Data Berhasil Di ubah','warning')
        return redirect(url_for('gadmin.anggota'))
    elif request.method=="GET":
        form.namaukm.data=dataukm.nama_ukm
        form.noizin.data=dataukm.no_izin
        form.industriid.data=dataukm.ukms.industri
        form.namapemilik.data=dataukm.nama_pemilik
        form.noktp.data=dataukm.no_ktp
    return render_template('t_admin/eanggota.html', form=form)

#batas CRUD Anggota UKM


#CRUD kategori

@gadmin.route("/kategori", methods=['GET', 'POST'])
def kategori():
    form=kategori_F()
    data=Tkategori.query.all()
    return render_template("t_admin/kategori.html", datakategori=data, form=form)


#buatlah fungsi edit dan hapusnya!

# batas CRUD kategori




#CRUD admin
@gadmin.route("/admin", methods=['GET', 'POST'])
def admin():
    form=eadmin_F()
    dataadmin=Tadmin.query.all()
    return render_template("t_admin/admin.html", data=dataadmin, form=form)


@gadmin.route("/edithakakses/<int:ed_id>/update", methods=['GET', 'POST'])
def update_admin(ed_id):
    dataadmin=Tadmin.query.get_or_404(ed_id)
    form=eadmin_F()
    if form.validate_on_submit():
        cekpass= Tadmin.query.filter_by(password=form.password.data).first()
        if cekpass and bcrypt.check_password_hash(cekpass.password, form.password.data):
            pass_hash= bcrypt.generate_password_hash(form.passwordbaru.data). decode('utf-8')
            dataadmin.username=form.usernamebaru.data
            dataadmin.password=pass_hash
            db.session.commit()
            flash('Hak Akses Berhasil di ubah','warning')
            return redirect(url_for('gadmin.dasboard'))
        else:
            flash('password yang dimasukan salah, silahkan coba kembali !!','danger')
            return redirect(url_for('gadmin.admin'))
       
    return render_template("t_admin/eadmin.html", data=dataadmin, form=form)

#batas crud admin