from flask import Flask, jsonify, request, json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from database import Members, Base
from werkzeug.utils import secure_filename

import pandas as pd

from logging.handlers import RotatingFileHandler
import os, logging

app = Flask(__name__)

engine = create_engine('sqlite:///test_app.db', echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# LOG FILE INFO
handler = RotatingFileHandler(os.environ['LOG_FILE'], maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# GET all members by account id
@app.route('/get_members_by_account_id/<int:account_id>', methods=['GET'])
def get_members_by_account_id(account_id):
    error = None
    try:
        query = session.query(Members).filter_by(account_id=account_id)
        member_data = session.execute(query)
        app.logger.info('GET MEMBER BY ACCOUNT ID')
        return jsonify({'members': [dict(row) for row in member_data]})
    except Exception as error:
        return error

# GET member by client_member_id and value
@app.route('/get_member_by_id/<int:id>', methods=['GET'])
def get_member_by_id(id):
    error = None
    try:
        query = session.query(Members).filter_by(id=id)
        member_data = session.execute(query)
        app.logger.info('GET MEMBER BY MEMBER ID')
        return jsonify({'member': [dict(row) for row in member_data]})
    except Exception as error:
        return error


# GET member by phone_number and value
@app.route('/get_member_by_phone_number/<int:number>', methods=['GET'])
def get_member_by_phone_number(number):
    error = None
    try:
        query = session.query(Members).filter_by(phone_number=number)
        member_data = session.execute(query)
        app.logger.info('GET MEMBER BY PHONE NUMBER')
        return jsonify({'member': [dict(row) for row in member_data]})
    except Exception as error:
        return error

# GET member by client_member_id and value
@app.route('/get_member_by_client_member_id/<int:client_member_id>', methods=['GET'])
def get_member_by_client_member_id(client_member_id):
    error = None
    try:
        query = session.query(Members).filter_by(client_member_id=client_member_id)
        member_data = session.execute(query)
        app.logger.info('GET MEMBER BY  CLIENT MEMBER ID')
        return jsonify({'member': [dict(row) for row in member_data]})
    except Exception as error:
        return error

# POST Add member
@app.route('/add_member', methods=['POST'])
def add_member():
    error = None
    if request.method == 'POST':
        try:
            request_param = json.loads(request.get_data(as_text=True))
            member = Members(first_name=request_param['first_name'],
                           last_name=request_param['last_name'],
                           phone_number=request_param['phone_number'],
                           client_member_id=request_param['client_member_id'],
                           account_id=request_param['account_id'])
            session.add(member)
            session.commit()
            session.close()
            return 'Added'
        except Exception as error:
            return error
    else:
        return "POST ONLY"

@app.route('/upload_members', methods=['POST'])
def upload_members():
    error = None
    if request.method == 'POST' and request.files.get('file'):
        member_csv_data = pd.read_csv(request.files.get('file'))
        app.logger.info('GOT CSV FILE')
        # remove phone_number per account_id duplicate
        member_csv_data.drop_duplicates(subset=['account_id', 'phone_number'], keep='first', inplace=True)
        app.logger.info('REMOVE DUPLICATE PHONE NUMBER ')
        # remove client_member_id per account_id duplicate
        member_csv_data.drop_duplicates(subset=['account_id', 'client_member_id'], keep='first', inplace=True)
        app.logger.info('REMOVE DUPLICATE CLIENT MEMBER ID')
        new_columns = [column.replace(' ', '_').lower() for column in member_csv_data]
        member_csv_data.columns = new_columns

        try:
            member_csv_data.to_sql("members",
                               engine,
                               index_label='id',
                               if_exists='append',
                               index=False,
                               chunksize=1000,
                               dtype={"first_name": String(50),
                                      "last_name": String(50),
                                      "phone_number": Integer,
                                      "client_member_id": Integer,
                                      "account_id": Integer})
        except Exception as e:
            existing = pd.read_sql('members', engine)
            join_bool = ~member_csv_data.id.isin(existing.id)
            try:
                member_csv_data.loc[join_bool].to_sql("members",
                                       engine,
                                       index_label='id',
                                       if_exists='append',
                                       index=False,
                                       chunksize=1000,
                                       dtype={"first_name": String(50),
                                              "last_name": String(50),
                                              "phone_number": Integer,
                                              "client_member_id": Integer,
                                              "account_id": Integer})
            except Exception as e:
                app.logger.info('FAILD TO UPLOAD DATA')
                return "Failed:"
        return 'Data Uploaded'


@app.errorhandler(404)
def page_not_found(e):
    return "404 - Check request data"

@app.errorhandler(500)
def page_not_found(e):
    return "500 - Internal server error"

app.run(host='0.0.0.0', port=5000, debug=True)

