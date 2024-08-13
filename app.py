from flask import Flask, render_template

app = Flask(__name__)

JOBS=[
  {'id':1, 'title':'Data Analyst', 'location':'Bengaluru, India',
   'salary': 'Rs. 4lpa'
  },
  {'id':2, 'title':'Machine Learning Engineer', 'location':'Pune, India'
  },
  {'id':3, 'title':'Python Devloper', 'location':'Hyderabad, India',
   'salary': 'Rs. 5lpa'
  },
  {'id':4, 'title':'Data Scientis', 'location':'Indore, India',
   'salary': 'Rs. 10lpa'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html',jobs=JOBS)




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
