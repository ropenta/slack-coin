import os
import psycopg2
import urllib.parse as ul


ul.uses_netloc.append("postgres")
url = ul.urlparse(os.environ["postgres://itlnykuwjunoll:a5bd6c66146478a7b4b202a0e59f0789536a746093495e22c1ba0bebca8af3ac@ec2-23-23-225-12.compute-1.amazonaws.com:5432/dbli9ucgjn3501"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rohith/Developer/slackbot/python_new/example.db'
# db = SQLAlchemy(app)

# class ExampleTable(db.Model):
#     id = db.Column(db.Integer, primary_key = True)

