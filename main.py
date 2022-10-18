# Import Packages
from flask import Flask, redirect, render_template, request

# Initialization
app = Flask(__name__)

# Routes
## Show the HTML
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")
    
@app.route("/aslab_admin", methods=["GET", "POST"])
def aslab_admin():
    return render_template("aslab_admin.html")
    
@app.route("/aslab_edit", methods=["GET", "POST"])
def aslab_edit():
    return render_template("aslab_edit.html")
    
@app.route("/aslab_tambah", methods=["GET", "POST"])
def aslab_tambah():
    return render_template("aslab_tambah.html")
    
@app.route("/jumbotron_admin", methods=["GET", "POST"])
def jumbotron_admin():
    return render_template("jumbotron_admin.html")

@app.route("/jumbotron_edit", methods=["GET", "POST"])
def jumbotron_edit():
    return render_template("jumbotron_edit.html")
    
@app.route("/jumbotron_tambah", methods=["GET", "POST"])
def jumbotron_tambah():
    return render_template("jumbotron_tambah.html")
    
@app.route("/kelas", methods=["GET"])
def kelas():
    return render_template("kelas.html")
    
@app.route("/kelas_admin", methods=["GET", "POST"])
def kelas_admin():
    return render_template("kelas_admin.html")
    
@app.route("/kelas_edit", methods=["GET", "POST"])
def kelas_edit():
    return render_template("kelas_edit.html")
    
@app.route("/kelas_tambah", methods=["GET", "POST"])
def kelas_tambah():
    return render_template("kelas_tambah.html")
    
@app.route("/kontak", methods=["GET"])
def kontak():
    return render_template("kontak.html")
    
@app.route("/modul", methods=["GET"])
def modul():
    return render_template("modul.html")
    
@app.route("/modul_admin", methods=["GET", "POST"])
def modul_admin():
    return render_template("modul_admin.html")
    
@app.route("/modul_tambah", methods=["GET", "POST"])
def modul_tambah():
    return render_template("modul_tambah.html")
    
@app.route("/pengaduan", methods=["GET"])
def pengaduan():
    return render_template("pengaduan.html")
    
@app.route("/pengaduan_admin", methods=["GET", "POST"])
def pengaduan_admin():
    return render_template("pengaduan_admin.html")

## API for Processing Data


# APP Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)