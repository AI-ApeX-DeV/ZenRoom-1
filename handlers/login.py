from zenroom.forms import Login
from zenroom import app, bcrypt
from flask import render_template, redirect, url_for, flash, request, session
import pymongo

client = pymongo.MongoClient('mongodb+srv://zenroom:Si1Gly32eKOO4WM3@cluster0.nt5nnqv.mongodb.net/')
db = client['zenroom']
col = db["users"]       



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        try:
            res = col.find({"email": form.email.data})
            session['user_id'] = res[0]["user_id"]
        except:
            flash('Incorrect Email/Password', "error")
            # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            # print(hashed_password, bcrypt.chec
            # k_password_hash("$2b$12$gbVs1yn4KeOxk2vkwXiYFuLCsrE/pHdlOK3Z3EDRGXMLnb.cT1P1W", form.password.data))
            print(res)
            return redirect(url_for('login'))
     

    
    return render_template('login.html', form= form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Login()
    session.permanent = True
    # session["user_id"] = user_id
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        return redirect(url_for('login'))
    
    return render_template('login.html', form= form)

