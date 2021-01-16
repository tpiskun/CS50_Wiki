# Project 1

Project1 Submission (Wiki) for the 2020 version of Harvard's CS50: Web Programming with Python and JavaScript Course.

## Motivation
 Combined with an internal drive to learn more about front end development as well as a required component to the CS50 course, this project is a deeper example of leveraging python and html for front-end development.The goal of this project is to reverse engineer Wikipedia to allow a user to view, edit, and create a wiki page. This user can also lookup a page that is generated randomly by selecting the random page link.

## Build Status
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)

## Features
This application contains the following features:
* Entry Page: By visiting the url of the entry page `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, a page is rendered and displays the contents of that encyclopedia entry.
  * If an entry that does not exist is requested, the user will be presented with an error page that indicates that their page was not found.
  * If the entry does exist, the user will be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
* Index Page: Contains a listing of the names of all the entries in the encyclopedia
  * User can click on any of these active links to view the actual entry page
* Search: Allows the user to type a query into the search box
  * If the query matches the name of an encyclopedia entry, the user will be redirected to that entry’s page.
  * If the query does not match the name of an encyclopedia entry, the user instead will be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring.
  * Clicking on any of the entry names on the search results page will take the user to that entry’s page.
* New Page: When clicking on “Create New Page”, the user will be redirected to a page where they can create a new encyclopedia entry.
  * Users can enter a title and content for their Wiki in Markdown
    * Markdown content will be automatically converted into an HTML readable format
  * Users will click a button to save their new pages and can view their newly created Wiki
  * If an encyclopedia entry already exists with the provided title, the user will be presented with an error message
* Edit Page: On each entry page, the user will be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a `textarea`
  * The textarea will be pre-populated with the existing Markdown content of the page
  * The user will be able to click a button to save the changes made to the entry
  * Once the entry is saved, the user should be redirected back to that entry’s page
* Random Page: Clicking `Random Page` in the sidebar will take a user to a random encyclopedia entry.


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
