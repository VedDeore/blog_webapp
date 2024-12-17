from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import os
import math
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
load_dotenv()

local_server = True
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# SQL Alchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER_PATH')
db = SQLAlchemy(app)

# Email Service Configuration
app.config.update(
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_PORT = os.getenv('MAIL_PORT'),
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
)
mail = Mail(app)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    error=None;
    if "user" in session and session['user']=="admin":
        posts = Posts.query.all()
        return render_template("dashboard.html", posts=posts)
    
    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        
        # admin credentials
        if username!="admin" or userpass!="pass1":
            # set the session variable
            error = "Invalid Credentials"  
        else:
            session['user']=username
            posts = Posts.query.all()
            return render_template("dashboard.html", posts=posts)
        
    return render_template("login.html",error=error)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(3))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(3):(page-1)*int(3)+ int(3)]
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    
    return render_template('index.html', posts=posts, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html')

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New blog contact message from ' + name, sender=email, recipients = ["{your_email_address}"], body = "Name : " + name + "\n" + "Contact Number : " + phone + "\n" + "Email: " + email + "\n" + "Message : " + message)
        flash("Thanks for submitting your details. We will get back to you soon", "success")
    return render_template('contact.html')

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)
    
@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post)

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user']=="admin":
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
                flash("Post added successfully", "success")
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.tagline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                flash("Post updated successfully", "success")
                return redirect('/edit/'+sno)
            
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', post=post, sno=sno)
    
@app.route("/delete/<string:sno>" , methods=['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user']=="admin":
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted successfully", "danger")
    return redirect("/dashboard")

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
    if "user" in session and session['user']=="admin":
        if request.method=='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            flash("Photo uploaded successfully", "success")
            return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

app.run(debug=True, use_reloader=False)