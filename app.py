import os
from flask import Flask, render_template, request, redirect
# from flask_compress import Compress
import urllib.request
from flask import g
import firebase_admin
from firebase_admin import credentials,firestore
from flask_mail import Mail,Message
import time
from datetime import date

app=Flask(__name__)
@app.route("/")
def home() : 
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)