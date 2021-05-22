from flask import Blueprint,request,redirect,url_for,jsonify
from app.db import books


book=Blueprint('book',__name__,url_prefix='/books')

@book.route('/get_books',methods=['GET'])
def get_books():
    lenght=len(books)
    return jsonify({'books':books, 'len':lenght}),200


@book.route('/add/<book>', methods=['POST','GET'])
def add_book(book):
    if request.method=='POST':
        print('making a post')
        # book=request.json['book']
        print(request.json)
        # books.append(book)
    else:
        print('Its just a get or other shit')
    return redirect(url_for('book.get_books')), 201

@book.route('book.delete_book',methods=['DELETE'])
def delete_book():
    books.pop()
    return redirect(url_for('book.get_books'))
