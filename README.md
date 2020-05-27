# Project 1

Project1 Submission for Harvard's CS50: Web Programming with Python and JavaScript Course.

## Motivation
 Combined with an internal drive to learn more about front end development as well as a required component to the CS50 course, this project is a deeper example of leveraging python and html for front-end development.The goal of this project is to build a website that is a book review that allows a user to register an account, login, leave reviews as well as retrieve other reviews from a third-party API called GoodReads.

## Build Status
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)

## Features
This project creates 3 SQL Databases with 3 tables:
  -users
  -books
  -reviews

There is a file called create.py that is a script that creates these SQL databases and models.py that outlines the table name and columns in a Python class.

Additionally, there is a file called import.py that imports all of the 5000 books that should be included in the "books" SQL database. To avoid manually inserting each book into the table, the import.py script handles it in an ad-hoc instance.

## Installation
This project requires flask. Once flask is installed, you will also need a database to store your table values. For this project, I used a Heroku database.

## API Reference
Since this project refers to the API on GoodReads, here is the documentation that was used:
  https://www.goodreads.com/api

I used the get book.review_counts API method to get the statistics I needed.

## How to Use?
This is to be run using flask with the following parameters:

```
$ export FLASK_APP=application.py
```
```
$ export FLASK_ENV=development
```
```
$ export DATABASE_URL= <Heroku Database Credentials>
```
```
$ Flask Run
```

## Credits
Source Code provided by Harvard's CS50 curriculum and professor Brian Yu.
