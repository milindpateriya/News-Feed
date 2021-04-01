import sqlite3

def adddata(name,us,pas,gen,sp,po,ent,sci):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    en=(name,us,pas,gen)
    em=(us,sp,ent,po,sci)
    cur.execute("INSERT INTO user(name,username,password,gender) VALUES(?,?,?,?)", en)
    cur.execute("INSERT INTO userint(username,sports,entertainment,politics,science) VALUES(?,?,?,?,?)", em)
    conn.commit()
    conn.close()

def readdata(us):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=?", (us,))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

def read_int(us):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute("SELECT sports,entertainment,politics,science FROM userint WHERE username=?", (us,))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row


conn = sqlite3.connect('user.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE if not exists user(
                name text NOT NULL,
                username blob PRIMARY KEY NOT NULL,
                password blob NOT NULL,
                gender text)
                """)
cur.execute("""CREATE TABLE if not exists userint(
                    username blob PRIMARY KEY,
                    sports integer,
                    entertainment integer,
                    politics integer,
                    science integer)    
                """)
conn.commit()
conn.close()




