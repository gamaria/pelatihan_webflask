from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from ukmummu import app
from ukmummu.models import Tindustri, Tukm, Tkategori, Tproduk, Tadmin

gadmin= Blueprint('gadmin',__name__)

@gadmin.route("/tes")
def tes():
    return "Selamat datang di pelatihan"

@gadmin.route("/dasboard")
def dasboard():
    return render_template("t_admin/base.html")

@gadmin.route("/industri")
def industri():
    data=Tindustri.query.all()
    return render_template("t_admin/industri.html", dataidustri=data)

@gadmin.route("/anggota")
def anggota():
    data=Tukm.query.all()
    return render_template("t_admin/anggota.html", dataukm=data)

@gadmin.route("/kategori")
def kategori():
    data=Tkategori.query.all()
    return render_template("t_admin/kategori.html", datakategori=data)