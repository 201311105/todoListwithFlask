import json, pymysql

conn = None

def getConnection():
        return pymysql.connect(host='localhost', user='root', password='1234',\
        db='todo', charset='utf8')

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def getauth(userid, passwd):
    global conn
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from users where userid = %s and passwd = %s"

    curs.execute(sql, (userid, passwd))
    rows = curs.fetchall()
    if rows:
        return True
    else:
        return False

def getScheduler(userid):
    global conn
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from todolist where userid = %s"
    
    curs.execute(sql, (userid))
    rows = curs.fetchall()
    return rows

def deleteSchedule(userid, data):
    global conn
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "delete from todolist where userid = %s and seq = %s"
    for d in data:
        curs.execute(sql, (userid, d))
    conn.commit()
    
def insertSchedule(data):
    global conn
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "insert into todolist (userid, priority, title, contain, deadline) \
    values (%s, %s, %s, %s, %s)"
    curs.execute(sql, (data[0], data[1], data[2], data[3], data[4]))
    conn.commit()

def signUp(userid, passwd):
    global conn
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from users where userid = %s"
    row = curs.execute(sql, (userid))
    if row:
        return False
    else:
        sql = "insert into users values (%s, %s)"
        curs.execute(sql, (userid, passwd))
        conn.commit()
        return True

def modifySchedule(data):
    global conn
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "update todolist set priority = %s, title = %s, contain = %s, deadline = %s, isDone = %s\
    where seq = %s"
    for d in data:
        print(d)
        curs.execute(sql, (d[0], d[1], d[2], d[3], d[4], d[5]))
    conn.commit()