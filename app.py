# https://www.tutorialspoint.com/flask/flask_templates.htm
import psycopg2
from flask import *

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

@app.route('/result')
def result():
   conn = psycopg2.connect(host="jonasdbflex.postgres.database.azure.com", port="5432", dbname="addresses", user="phoneman", password="Splunk6615_",  sslmode="require")
   C = conn.cursor()
   C.execute("SELECT * FROM phonelist;")
   record = C.fetchone()
   print(record)

   dict = {} 
   for x, y in pairwise(record):
      dict[x] = y
   
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)


