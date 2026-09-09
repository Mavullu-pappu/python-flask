#import flask class
from flask import Flask, render_template,request,redirect, url_for
import mysql.connector as mysql
#create connection
con=mysql.connect(host="localhost",user="root",password="Phani692004",database="employee_fp56")
# create the object of the flask class
app = Flask(__name__)

@app.route('/') #defalut page when we run the server
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/data',methods=['GET','POST'])
def data():
    cur=con.cursor()
    cur.execute("select * from employee")
    employee=cur.fetchall()
    return render_template('data.html',result=employee)

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        mobilno = request.form['mobilno']
        location = request.form['location']
        zipcode = request.form['zipcode']
        #create cursor
        cur=con.cursor()
        query="""insert into employee(firstname,lastname,email,mobilno,password,location,zipcode) 
           values(%s,%s,%s,%s,%s,%s,%s)"""
        values=(firstname,lastname,email,mobilno,password,location,zipcode)
        # Here you can process the data, e.g., save it to a database
        cur.execute(query, values)
        con.commit()# save the operator

        return redirect(url_for('login') ) # Redirect to dashboard after successful signup
    return render_template('signup.html')
    
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    cur=con.cursor()
    query="select * from employee where id=%s"
    values=(id,)
    cur.execute(query,values)
    employee=cur.fetchone()
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        mobilno = request.form['mobilno']
        location = request.form['location']
        zipcode = request.form['zipcode']
        query="""update employee set firstname=%s,lastname=%s,email=%s,password=%s,
        mobilno=%s,location=%s,zipcode=%s where id=%s"""
        values=(firstname,lastname,email,password,mobilno,location,zipcode,id)
        cur.execute(query,values)
        con.commit()
        return redirect(url_for('data'))
    return render_template('update.html',result=employee)        
       
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    cur=con.cursor()
    query='delete from employee where id=%s'
    values=(id,)
    cur.execute(query,values)
    con.commit()
    return redirect(url_for('data'))

    
    # run the flask app
if __name__=="__main__":
    app.run(debug=True)