# Project 1

Project1 Submission (Wiki) for the 2020 version of Harvard's CS50: Web Programming with Python and JavaScript Course.

## Motivation
 Combined with an internal drive to learn more about front end development as well as a required component to the CS50 course, this project is a deeper example of leveraging python and html for front-end development.The goal of this project is to reverse engineer Wikipedia that allows a user to view, edit, and create a wiki page. This user can also lookup a page that is generated randomly by selecting the random page link.

## Build Status
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)

## Features
This project allows the user to:
  * Lookup an Existing Wiki
  * Edit an Existing Wiki
  * Create a new Wiki
  * Select a Wiki at Random
  * Search for a Wiki using a search bar
  * Can find a wiki based of text matching
  * Visit a wiki by typing in the specific URL
  * User writes the Wiki in Markdown and the Application converts it automatically

Leveraging pre-existing Django features, there is a file called views.py that outlines all of the Python methods and functionalities.

Additionally, there is a file called urls.py that maintains all of the different possible URLs in the application which is called Encyclopedia.

Lastly, there is an entries folder which contains all of the markup .md files which contains the data for the HTML pages. The actual HTML files for these pages are automatically populated and stored in the templates file.

## Installation
This project requires Django.

## API Reference
Since this project uses Django, I used the Django documentation to research and clarify any additional features and functionality used in this project:
  https://docs.djangoproject.com/en/3.0/

## How to Use?
This is to be run just like any other Django application. After locating the manage.py file in the application directory, run the following command in terminal:

```
$ python manage.py runserver
```

## Credits
Source Code provided by Harvard's CS50 curriculum and professor Brian Yu.
