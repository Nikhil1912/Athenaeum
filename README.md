# Athenaeum
[![DOI](https://zenodo.org/badge/544187336.svg)](https://zenodo.org/badge/latestdoi/544187336)

Athenaeum is an application dedicated to connecting you with the textbooks you're searching for. We search the web far and wide to find textbooks, along with their distributors and prices. Using Athenaeum, you can simplify your journey and minimize your costs as you find the resources you need for class.

Currently, to get everything up and running:
* Install dependencies. 
   * The easiest way to do this: navigate to \Athenaeum and run `pip install -r requirements.txt`
   * [Node.js](https://nodejs.org/en/download/) includes npm (v. 8.15.0), which is also required.
* To run the backend:
   * Navigate to the backend directory
   * Create a new file `\Athenaeum\backend\.env` and add the secret key in the file:
     * `SECRET_KEY = '<secret key>'`
     * NOTE: the file should be entitled `.env`, NOT `backend.env`
   * If running for the first time, run the migrate commands (if confused, review help [here](https://stackoverflow.com/questions/56166319/oserror-winerror-123-the-filename-directory-name-or-volume-label-syntax-is))
   * Run `python manage.py runserver`
   * Navigate to http://localhost:8000/api/books/
   To stop the server, hit CTRL+C
* To run the frontend:
   * Navigate to the frontend directory
   * Run `npm ci`
   * Run `npm start`
   * Navigate to http://localhost:3000
   * To leave, hit CTRL+C and then Y

You can currently add, edit, or delete a book from the frontend.
