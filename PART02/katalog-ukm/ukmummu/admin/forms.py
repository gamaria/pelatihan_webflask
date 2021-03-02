from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#from sim.models import Tmahasiswa
#from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


#sesi pelatihan
class kategori_F(FlaskForm):
    kategori= StringField('Kategori', validators=[DataRequired()])
    keterangan= TextAreaField('Keterangan')
    submit=SubmitField('Tambah')


class ukm_F(FlaskForm):
    no_ktp= StringField('Kategori', validators=[DataRequired()])
    nama= TextAreaField('Keterangan')
    submit=SubmitField('Tambah')