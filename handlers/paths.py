from flask import render_template, flash, redirect, url_for, session
from zenroom import app
# hello


@app.route("/exercise")
def exercise():
    if not session.get("name"):
        flash("you must be logged in", "error")
        return redirect(url_for("login"))
    return render_template('exercise.html', title='Exercises to improve you mental health')


@app.route('/therapy')
def therapy():
    if not session.get("name"):
        flash("you must be logged in", "error")
        return redirect(url_for("login"))
    return render_template('bot.html')


@app.route('/map')
def map():
    if not session.get("name"):
        flash("you must be logged in", "error")
        return redirect(url_for("login"))
    return render_template('map.html')


@app.route('/user_dashboard')
def user_dashboard():
    if not session.get("name"):
        flash("you must be logged in", "error")
        return redirect(url_for("login"))
    return render_template('user_dashboard.html')
