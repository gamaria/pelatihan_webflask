from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ukmummu.models import Tukm, Tindustri, Tkategori, Tadmin
from flask_wtf.file import FileField, FileAllowed

#form inputan
class industri_F(FlaskForm):
    industri= StringField('Industri', validators=[DataRequired()])
    ket= TextAreaField('Keterangan')
    submit=SubmitField('Tambah')

    #cek industri
    def validate_industri(self, industri):
        cekindustri=Tindustri.query.filter_by(industri=industri.data).first()
        if cekindustri:
            raise ValidationError('Industri Sudah Terdaftar!')

class ukm_F(FlaskForm):
    namaukm= StringField('Nama UKM', validators=[DataRequired()])
    noizin= StringField('No Izin', validators=[DataRequired()])
    industriid= SelectField('industri', choices=[], validators=[DataRequired()])
    namapemilik= StringField('Nama Pemilik', validators=[DataRequired()])
    noktp= StringField('No KTP',validators=[DataRequired()])
    submit=SubmitField('Tambah')

    #cek no izin
    def validate_noizin(self, noizin):
        ceknoizin=Tukm.query.filter_by(no_izin=noizin.data).first()
        if ceknoizin:
            raise ValidationError('No Izin Sudah Terdaftar!')


class kategori_F(FlaskForm):
    kategori= StringField('Kategori', validators=[DataRequired()])
    ket= TextAreaField('Keterangan')
    submit=SubmitField('Tambah')

    #cek industri
    def validate_kategori(self, kategori):
        cekkategori=Tindustri.query.filter_by(kategori=kategori.data).first()
        if cekkategori:
            raise ValidationError('Kategori Sudah Terdaftar!')


#form edit
class eindustri_F(FlaskForm):
    industri= StringField('Industri', validators=[DataRequired()])
    ket= TextAreaField('Keterangan')
    submit=SubmitField('Ubah')

class eukm_F(FlaskForm):
    namaukm= StringField('Nama UKM', validators=[DataRequired()])
    noizin= StringField('No Izin', validators=[DataRequired()])
    industriid= SelectField('industri', choices=[], validators=[DataRequired()])
    namapemilik= StringField('Nama Pemilik', validators=[DataRequired()])
    noktp= StringField('No KTP',validators=[DataRequired()])
    submit=SubmitField('Ubah')

class ekategori_F(FlaskForm):
    kategori= StringField('Kategori', validators=[DataRequired()])
    ket= TextAreaField('Keterangan')
    submit=SubmitField('Ubah')

    
class eadmin_F(FlaskForm):
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    usernamebaru= StringField('Username Baru', validators=[DataRequired()])
    passwordbaru= PasswordField('Password Baru', validators=[DataRequired(), Length(min=5)])
    submit=SubmitField('Ubah')

    def validate_username(self, username):
        cekadmin=Tadmin.query.filter_by(username=username.data).first()
        if not cekadmin:
            raise ValidationError('username yang anda masukan salah!')
    
    


#and bcrypt.check_password_hash(cekadmin.password, password.data):