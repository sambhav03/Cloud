# how to create a website
import flask
app=flask.Flask('MyApp')
@app.errorhandler(404)
def errorpage(err):
    return 'Page under Construction'
@app.route('/')
def indexpage():
    return '<h1>Welcome to my Page</h1>'
@app.route('/about')
def aboutpage():
    return '<h5>This is About<h5>'
@app.route('/login')
def loginpage():
    return '''
    <form action='/verify' method='post'>
    username:<input type='text' name='uname'/><br/>
    password:<input type='password' name='pw'/><br/>
    <input type='submit' value ='LOGIN'/>
    </form>'''
@app.route('/verify',methods=['post'])
def verifypage():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not(u=='abc' and p=='xyz'):
        return  'LOGIN FAILED'
    else:

        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('select * from logdata')
        result=cur.fetchall()
        return flask.render_template('report.html',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\Users\lab365\Desktop\PythonTraining\bin',filename=filename)
@app.route('/empid/<int:eid>')
def empid(eid):
    D={'name':'sambhav','empid':eid}
    return D

@app.route('/logdata')
def logdata():
    return flask.redirect('/login')
@app.route('/passwords')
def passwords():
    return flask.abort(201,'Access Denied')

app.run()

