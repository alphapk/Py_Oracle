from flask import Flask, request, render_template, url_for, redirect, flash
import cx_Oracle

app = Flask(__name__)
app.secret_key = "flash_message"


@app.route("/")
def index():



    return render_template('index.html')

@app.route('/records',methods=['POST','GET'])
def records():
    if request.method == "POST":
     flash("retreived succesfully")
     cor_id = request.form['v1']
     incor_id = request.form['v2']
     conn = cx_Oracle.connect("hr/hr@localhost/pdborcl")
     cur = conn.cursor()
     params={'v1':cor_id,'v2':incor_id}
     cur.execute("select employee_id,first_name,last_name from employees where employee_id in (:v1,:v2)",params)
     employees = cur.fetchall()
     conn.close()
     return redirect(url_for('index',cor_id=cor_id,incor_id=incor_id,emps=employees))




if __name__ == "__main__":
    app.debug = True
    app.run()




