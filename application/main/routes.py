from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId

from ..extensions import mongo

main = Blueprint('main',__name__)



@main.route('/')
def index():
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos = todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo_item = request.form.get('add_todo')
    todos_collection.insert_one({'text': todo_item, 'complete':False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todos
    todos_collection.update_one({"_id": ObjectId(oid)}, {"$set": {"complete": True}})

    return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    todos_collection = mongo.db.todos
    todos_collection.delete_many({'complete':True})
    return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
    todos_collection = mongo.db.todos
    todos_collection.delete_many({})
    return redirect(url_for('main.index'))

@main.route('/sign_in')
def sign_in():
    
    return render_template('login.html')
