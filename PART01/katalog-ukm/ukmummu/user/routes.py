from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from ukmummu import app

guser= Blueprint('guser',__name__)

@guser.route("/")
def home():
    return "Hello Ini halaman untuk user"