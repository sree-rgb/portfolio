import os
import requests
from flask import Flask, jsonify, render_template, request, session, redirect,url_for,send_file,send_from_directory

app=Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")