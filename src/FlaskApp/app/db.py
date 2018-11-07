import json, pymysql


def connection():
        conn = pymysql.connect(host='localhost', user='root', password='1234',\
        db='todo', charset='utf8')
        return conn

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def getauth(conn, userid, passwd):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from users where userid = %s and passwd = %s"

    curs.execute(sql, (userid, passwd))
    curs.close()
    rows = curs.fetchall()
    if rows:
        return True
    else:
        return False

def getScheduler(conn, userid):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from todolist where userid = %s"
    
    curs.execute(sql, (userid))
    rows = curs.fetchall()
    curs.close()

    return rows

def deleteSchedule(conn, userid, data):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "delete from todolist where userid = %s and seq = %s"
    for d in data:
        curs.execute(sql, (userid, d))
    curs.close()
    conn.commit()
    
def insertSchedule(conn, data):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "insert into todolist (userid, priority, title, contain, deadline) \
    values (%s, %s, %s, %s, %s)"
    curs.execute(sql, (data[0], data[1], data[2], data[3], data[4]))
    curs.close()
    conn.commit()

def signUp(conn, userid, passwd):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from users where userid = %s"
    row = curs.execute(sql, (userid))
    if row:
        return False
    else:
        sql = "insert into users values (%s, %s)"
        curs.execute(sql, (userid, passwd))
        curs.close()
        conn.commit()
        return True

def modifySchedule(conn, data):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "update todolist set priority = %s, title = %s, contain = %s, deadline = %s, isDone = %s\
    where seq = %s"
    for d in data:
        print(d)
        curs.execute(sql, (d[0], d[1], d[2], d[3], d[4], d[5]))
        
    curs.close()
    conn.commit()