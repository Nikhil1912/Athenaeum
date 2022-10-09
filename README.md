# Athenaeum
[![DOI](https://zenodo.org/badge/544187336.svg)](https://zenodo.org/badge/latestdoi/544187336)
<a href="https://github.com/Nikhil1912/Athenaeum/main/LICENSE.md"><img src="https://img.shields.io/github/license/Nikhil1912/CSC510-HW_37?style=plastic" /></a>
![GitHub issues](https://img.shields.io/github/issues/Nikhil1912/Athenaeum)
![Repo Size](https://img.shields.io/github/repo-size/Nikhil1912/Athenaeum?color=brightgreen)
[![Unit tests](https://github.com/Nikhil1912/Athenaeum/actions/workflows/backend-tests.yml/badge.svg)](https://github.com/Nikhil1912/Athenaeum/actions/workflows/backend-tests.yml)
[![codecov](https://codecov.io/gh/Nikhil1912/Athenaeum/branch/main/graph/badge.svg?token=5UIM8QKSNQ)](https://codecov.io/gh/Nikhil1912/Athenaeum)

## Motivation
Athenaeum is an application dedicated to connecting you with the books you're searching for. Our goal: to search the web and find you the books you seek at a reputable distributor and a good price. Using Athenaeum, you can simplify your journey and minimize your costs as you find the resources you need for class.

## Current scope and Future Work
At present, you can add, edit, or delete a book from your local machine. If the book has a link to purchase, the "Buy" button will direct you to the appropriate page. If you search for a book that exists in our database, it will direct you to the appropriate Wikipedia link for that book. 

Our web scraper is currently in progress, but we intend to integrate it with our current page to allow for a more optimized searching experience that also presents pricing. We also intend to create a "Buy/Sell" user forum, as well as a login page.

## Running Athenaeum
Currently, to get everything up and running:
* Install dependencies. 
   * The easiest way to do this: navigate to `\Athenaeum` and run `pip install -r requirements.txt`
   * [Node.js](https://nodejs.org/en/download/) includes npm (v. 8.15.0), which is also required.
* To run the backend:
   * Navigate to the backend directory, `\Athenaeum\backend`
   * Create a new file `\Athenaeum\backend\.env` and add the secret key in the file:
     * `SECRET_KEY = '<secret key>'`
     * NOTE: the file should be entitled `.env`, NOT `backend.env`
   * If running for the first time, run the migrate commands (if confused, review help [here](https://stackoverflow.com/questions/56166319/oserror-winerror-123-the-filename-directory-name-or-volume-label-syntax-is))
   * Run `python manage.py runserver`
   * Navigate to http://localhost:8000/api/books/
   To stop the server, hit CTRL+C
* To run the frontend:
   * Navigate to the frontend directory, `\Athenaeum\frontend`
   * If running for the first time, run `npm ci`
   * Run `npm start`
   * Navigate to http://localhost:3000
   * To leave, hit CTRL+C and then Y
