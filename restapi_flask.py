#API 1 -->IPs
#api1=http://127.0.0.1:8080/ip
import flask
app=flask.Flask('MyApp')
@app.route('/ip',methods=['GET'])
def api_ip():
    import sqlite3
    con=sqlite3.connect('mydb.sqlite3')
    cur=con.cursor()
    cur.execute('select ip from logdata')
    result=cur.fetchall()
    #return str(result)
    result=[i[0] for i in result]
    d={k:v for k,v in enumerate(result)}
    return d
#api2-http://127.0.0.1:8080/emp
@app.route('/emp',methods=['POST'])
def empdetails():
    details=flask.request.args
    details=dict(details)
    return details
#api3
@app.route('/json')
def fromjson():
    f=open('mydata.json','w')
    d={'course':'python','loc':'blr'}
    import json
    json.dump(d,f)
    f.close()
    f=open('mydata.json')
    r=json.load(f)
    f.close()
    return r
app.run()
