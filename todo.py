from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from db import db, TodoList

bp = Blueprint('todo', __name__, url_prefix='/todo')
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('todo_id')
parser.add_argument('status')
parser.add_argument('due')

class Personal(Resource):
    def get(self, personal_id=1):
        result = []
        query = TodoList.query.filter_by(personal_id = personal_id).all()
        for todo in query:
            result.append({'id':todo.id, 'title':todo.title, 'content':todo.content, 'due':todo.due, 'status':todo.status})
        return jsonify(status = 'success', result=result)

    def post(self, personal_id=1):
        args = parser.parse_args()
        new_todo = TodoList()
        new_todo.title = args['title']
        new_todo.content = args['content']
        new_todo.personal_id = personal_id
        # login required 적용하고 new_todo.user_id = current_user.id 추가하기 
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'title':new_todo.title, 'content':new_todo.content})

    def put(self, personal_id=1):
        args = parser.parse_args()
        todo = TodoList.query.filter_by(id = args['todo_id']).first()
        todo.title = args['title']
        todo.content = args['content']
        todo.status = args['status']
        todo.due = args['due']
        db.session.commit()
        return jsonify(status = 'success', result = {'title':todo.title, 'content':todo.content, 'status':todo.status, 'due':todo.due})

    def delete(self, personal_id=1):
        args = parser.parse_args()
        todo = TodoList.query.filter_by(id = args['todo_id']).first()
        db.session.delete(todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'id':args['todo_id'], 'title':args['title']})

class Group(Resource):
    def get(self, group_id):
        result = []
        query = TodoList.query.filter_by(group_id = group_id).all()
        for todo in query:
            result.append({'id':todo.id, 'title':todo.title, 'content':todo.content, 'due':todo.due, 'status':todo.status})
        return jsonify(status = 'success', result=result)

    def post(self, group_id):
        args = parser.parse_args()
        new_todo = TodoList()
        new_todo.title = args['title']
        new_todo.content = args['content']
        new_todo.group_id = group_id
        # login required 적용하고 new_todo.user_id = current_user.id 추가하기 
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'title':new_todo.title, 'content':new_todo.content})

    def put(self, group_id):
        args = parser.parse_args()
        todo = TodoList.query.filter_by(id = args['todo_id']).first()
        todo.title = args['title']
        todo.content = args['content']
        todo.status = args['status']
        todo.due = args['due']
        db.session.commit()
        return jsonify(status = 'success', result = {'title':todo.title, 'content':todo.content, 'status':todo.status, 'due':todo.due})

    def delete(self, group_id):
        args = parser.parse_args()
        todo = TodoList.query.filter_by(id = args['todo_id']).first()
        db.session.delete(todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'id':args['todo_id'], 'title':args['title']})

api.add_resource(Personal, '/personal/<personal_id>')
api.add_resource(Group, '/group/<group_id>')