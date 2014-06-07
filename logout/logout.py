#encoding=utf8
import web,sae

class logout:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session
        global failed
        failed = '''{"success":0,"info":"%s"}'''

    def POST(self):
        try:
            session.login = False
            session.username = ''
            session.usertype = ''
            #web.seeother('/logIn.html')
            return '''{"success":1}'''
        except Exception as e:return failed%str(e)