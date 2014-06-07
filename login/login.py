#encoding=utf8
import web,sae
import sys,os
import MySQLdb
reload(sys)
abspath = os.path.dirname(__file__)
abspath += '/..'
sys.path.append(abspath)
sys.setdefaultencoding('utf-8')

from MySQL_API import SQL

class login:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session
        global failed
        failed = '''{"success":0,"info":"%s"}'''

    def POST(self):
        conn =  SQL.sacdb_init().getcon()
        cursor=conn.cursor()
        try:
            ID = web.websafe(web.input().userName)
            pw = web.websafe(web.input().pwd)
            cursor.execute("SELECT * FROM userlist WHERE ID = '%s' and password = '%s'"%(ID,pw))
            if cursor.rowcount ==1:
                V = cursor.fetchone()
                session.login = True
                session.ID = ID
                session.ehour = V[5]
                session.usertype = V[3]
                if session.usertype == 'admin':
                    web.seeother('/admin.html')
                elif session.usertype == 'student':
                    web.seeother('/home.html')
                else:
                    return 'sys error'
            else:
                return failed%'not exist'
        except Exception as e:return failed%str(e)
        finally:
            cursor.close()
            conn.close()