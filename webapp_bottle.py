# how to create a website
import bottle
app=bottle.Bottle()
@app.error(404)
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
@app.route('/verify',method='POST')
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not(u=='abc' and p=='xyz'):
        return  'LOGIN FAILED'
    else:
        bottle.TEMPLATE_PATH.append(r'C:\Users\lab365\Desktop\PythonTraining\bin')
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('select * from logdata')
        result=cur.fetchall()
        return bottle.template('report.tpl',res=result)#variable res will be accessible in tpl
@app.route('/download/<filename>')
def staticfile(filename):
    return bottle.static_file(root=r'C:\Users\lab365\Desktop\PythonTraining\bin',filename=filename)
@app.route('/empid/<eid:int>')
def empid(eid):
    D={'name':'sambhav','empid':eid}
    return D
@app.route('/nameid/<nid:re:[a-z0-9]+>')
def name_id(nid):
    return str(nid)
@app.route('/logdata')
def logdata():
    return bottle.redirect('/login')
@app.route('/passwords')
def passwords():
    return bottle.abort(201,'Access Denied')

app.run(host='192.168.3.73')

