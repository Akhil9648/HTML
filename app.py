from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db=SQLAlchemy(app)
# class Todo(db.moodel):
#     Sno=db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(200),Nullable=False)
#     desc=db.Column(db.String(500),Nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self)->str:
#          return f"{self.Sno} - {self.title}"
@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/products")
def products():
    return "<p>This is products page!</p>"
if __name__=="__main__":
    app.run(debug=True)
