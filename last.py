from flask import Flask, request, render_template, url_for, redirect, flash
import cx_Oracle

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    v1=''
    v2=''
    if request.method == 'POST':  #this block is only entered when the form is submitted
        v1 = request.form.get('v1')
        v2 = request.form['v2']
    #v1=100
    #v2=101
    conn = cx_Oracle.connect("hr/hr@localhost/pdborcl")
    cur = conn.cursor()
    params = {'v1': v1, 'v2': v2}
    cur.execute("select employee_id,first_name,last_name from employees where employee_id in (:v1,:v2)", params)
    employees = cur.fetchall()
    #sqlStr = """BEGIN pk_swap( :v1, :v2);
   # end;"""
    #cur.execute(sqlStr, params)
    #cur.execute('''BEGIN pk_swap(:v1,:v2); END; ''',params)
    conn.commit()
    cur.close()
    conn.close()
    return render_template('demo.html',empsv=employees)




if __name__ == "__main__":
    app.debug = True
    app.run()