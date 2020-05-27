import os
import requests
from flask import Flask, session, request, render_template, redirect, url_for, flash, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/" , methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        if session.get("user"):
            user_id=str(session["user"]).strip("[](),'")
            username=db.execute("SELECT username FROM users WHERE id = :id",{"id": user_id}).fetchone()
            usernamemsg=str(username).strip("[](),'")
            return render_template('index.html', message="Welcome Back", username=usernamemsg, session=session["user"])
        return render_template("index.html")
    else:
        form_username=request.form.get("usr")
        form_password=request.form.get("pass")
        db_data=db.execute("SELECT id FROM users WHERE username = :username AND password = :password", {"username": form_username, "password":form_password}).fetchone()

        if db_data is None:
            return render_template('Error.html', message="Invalid Username and Password.")
        else:
            session["user"]=db_data
            user_id=str(session["user"]).strip("[](),'")
            username=db.execute("SELECT username FROM users WHERE id = :id",{"id": user_id}).fetchone()
            usernamemsg=str(username).strip("[](),'")
            return redirect(url_for('index', message="Welcome back", username=usernamemsg, session=session["user"]))

@app.route("/Search", methods=['POST'])
def Search():
    if request.method=="POST":
        search_data=request.form.get("SearchBar")
        search="%" + search_data.lower() + "%"
        db_search_data =db.execute("SELECT * FROM books WHERE lower(title) LIKE :search OR lower(author) LIKE :search OR lower(isbn) LIKE :search",{"search": search}).fetchall()
        if len(db_search_data) > 0:
            return render_template("SearchResultList.html", books=db_search_data, resultQuery= search_data)
        else:
            return render_template("Error.html", message="No book found with that ISBN, title, or author.")

@app.route("/BookId/<int:Book_id>" , methods=['GET', 'POST'])
def BookId(Book_id):
    session.get("user")
    user_id=str(session["user"]).strip("[](),'")
    username=db.execute("SELECT username FROM users WHERE id = :id",{"id": user_id}).fetchone()
    usernamemsg=str(username).strip("[](),'")

    db_book_data = db.execute("SELECT * FROM books WHERE id = :id", {"id":Book_id}).fetchone()
    isbn=db_book_data[1]
    title = db_book_data[2]
    author= db_book_data[3]
    year= db_book_data[4]
    book=Book(isbn=isbn, title=title, author=author, year=year)
            #res = requests.get("https://www.goodreads.com/book/title.json", params={"key": "UCZJQxVrJtm6vEty8Yok7Q", "secret": "G6HZIbvGWU2Etp0QPOAH8U2F8pFwgUNqGUvksLEMo8" , "title": book.title, "author": book.author})
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "UCZJQxVrJtm6vEty8Yok7Q", "secret": "G6HZIbvGWU2Etp0QPOAH8U2F8pFwgUNqGUvksLEMo8" , "isbns": book.isbn})
    avg_rating=res.json()["books"][0]["average_rating"]
    num_of_ratings=res.json()["books"][0]["ratings_count"]
    db_review_data=db.execute("SELECT * FROM reviews WHERE book_id = :book_id" , {"book_id": Book_id}).fetchall()
    db_user_submission=db.execute("SELECT * FROM reviews WHERE user_id = :user_id AND book_id = :book_id", {"user_id" : user_id, "book_id": Book_id}).fetchone()

    if len(db_review_data) > 0:
        ReviewsExist=True
    else:
        ReviewsExist=False

    if db_user_submission is None:
        RatingExists=True
        if request.method=="POST":
            #review=str(res.json()["reviews_widget"]).rstrip()
            Rating=request.form.get("inputBookRating")
            RatingText=request.form.get("inputBookRatingText")
            user_review=Review(book_rating=Rating, book_rating_text=RatingText, book_id=Book_id, user_id=user_id, username=usernamemsg)
            db.add(user_review)
            db.commit()
            flash('Thank you for submitting your review. Keep browsing other titles and let us know what you think!')
            return redirect(url_for('index'))
            #return render_template("BookResult.html", Book=book, AverageRating=avg_rating, NumberOfRating=num_of_ratings , RatingExists=RatingExists, book_reviews=db_review_data , ReviewsExist=ReviewsExist)
        else:
            return render_template("BookResult.html", Book=book, AverageRating=avg_rating, NumberOfRating=num_of_ratings, RatingExists=RatingExists, book_reviews=db_review_data, ReviewsExist=ReviewsExist)
    else:
        RatingExists=False
        return render_template("BookResult.html", Book=book, AverageRating=avg_rating, NumberOfRating=num_of_ratings, RatingExists=RatingExists, book_reviews=db_review_data, ReviewsExist=ReviewsExist)

@app.route("/api/BookId/<int:Book_id>")
def BookId_api(Book_id):
    db_book_data = db.execute("SELECT * FROM books WHERE id = :id", {"id":Book_id}).fetchone()
    if db_book_data is None:
        return jsonify({"error": "Invalid Book_id"}), 422
    isbn=db_book_data[1]
    title = db_book_data[2]
    author= db_book_data[3]
    year= db_book_data[4]
    book=Book(isbn=isbn, title=title, author=author, year=year)
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "UCZJQxVrJtm6vEty8Yok7Q", "secret": "G6HZIbvGWU2Etp0QPOAH8U2F8pFwgUNqGUvksLEMo8" , "isbns": book.isbn})
    avg_rating=res.json()["books"][0]["average_rating"]
    num_of_ratings=res.json()["books"][0]["ratings_count"]
    return jsonify({
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "isbn": book.isbn,
        "review_count": num_of_ratings,
        "average_score": avg_rating
    })

@app.route("/Register" , methods=['GET', 'POST'])
def Register():
    if request.method=="GET":
        return render_template('Register.html')
    else:
        new_username=request.form.get("new_usr")
        new_password=request.form.get("new_pass")
        db_data=db.execute("SELECT id FROM users WHERE username = :username",
                                    {"username": new_username}).fetchone()
        if db_data is None:
            newuser=User(username=new_username, password=new_password)
            db.add(newuser)
            db.commit()
            db_data=db.execute("SELECT id FROM users WHERE username = :username AND password = :password",
                                        {"username": new_username, "password":new_password}).fetchone()
            session["user"]=db_data
            return render_template('Index.html', message="Welcome to GoodReads" , username=newuser.username, session=session["user"])
        else:
            return render_template('Error.html', message="Username Exists. Please choose a new name")

@app.route("/Logout")
def Logout():
    session.clear()
    #request.method is "GET"
    return redirect(url_for('index'))
