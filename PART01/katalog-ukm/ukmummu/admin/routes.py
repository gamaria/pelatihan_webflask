from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from ukmummu import app

gadmin= Blueprint('gadmin',__name__)

@gadmin.route("/tes")
def tes():
    return "Selamat datang di pelatihan"

@gadmin.route("/dasboard")
def dasboard():
    return render_template("t_admin/base.html")

@gadmin.route("/industri")
def industri():
    return render_template("t_admin/industri.html")

@gadmin.route("/anggota")
def anggota():
    return render_template("t_admin/anggota.html")

@gadmin.route("/kategori")
def kategori():
    return render_template("t_admin/kategori.html")