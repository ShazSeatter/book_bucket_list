from flask import Flask, render_template, request, redirect
from models.author import Author

import repositories.author_repository as author_repository

from flask import Blueprint

authors_blueprint = Blueprint("authors", __name__)



@authors_blueprint.route('/authors')
def authors():
    authors = author_repository.select_all()
    return render_template('authors/index.html', all_authors = authors)




# CRUD FUNCTIONALITY FOR CREATING NEW AUTHOR 

# # NEW
# # GET 'author/new'
@authors_blueprint.route('/authors/new')
def new_author():
    authors = author_repository.select_all()
    return render_template('authors/new.html', all_authors = authors)


# CREATE
# POST '/books'
@authors_blueprint.route('/authors', methods=['POST'])
def create_author():
   first_name = request.form['first-name']
   last_name = request.form['last-name']
   author = Author(first_name, last_name)
   author_repository.save(author)
   return redirect('/authors')