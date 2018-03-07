from flask import Flask,render_template,request
import MySQLdb
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/result',methods=['post'])
def result():
    roll=request.form['rollno']
    db=MySQLdb.connect("localhost","root","vishal55555","pythonflask", 3305)
    ob=db.cursor()
    query="select * from result where rollno="+roll
    ob.execute(query)
    return render_template('result.html',m=ob.fetchone())

if __name__=='__main__':
    app.run(debug=True,port=5000)
